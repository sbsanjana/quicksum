import flask
from flask import request
from flask_cors import cross_origin
# import speech_recognition as sr
import threading
import moviepy.editor as me
from google.cloud import speech
from google.cloud import storage
from pydub import AudioSegment
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
import string

app = flask.Flask(__name__)
# app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    # print(request.get_json()['string'])
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/upload', methods=['POST'])
@cross_origin()
def main():
    # print(request.get_data())
    vFile = (request.files['inputFile'])
    print(request.files['inputFile'])

    vFile.save('./video')
    VIDEO_FILE = './video'
    OUTPUT_AUDIO_FILE = "converted.wav"

    video_clip = me.VideoFileClip(r"{}".format(VIDEO_FILE))
    video_clip.audio.write_audiofile(r"{}".format(OUTPUT_AUDIO_FILE))

    sound = AudioSegment.from_wav('converted.wav')
    sound = sound.set_channels(1)
    sound.export('converted.wav', format="wav")
    client = speech.SpeechClient()
    transcript= ''
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('audiofiles_convert')

    blob = bucket.blob('fifth')
    storage.blob._MAX_MULTIPART_SIZE = 5 * 1024* 1024
    blob._chunk_size = 5 * 1024* 1024
    blob.upload_from_filename('/Users/sanjanabadhya/convert/api/converted.wav')
    gcs_uri = 'gs://' + 'audiofiles_convert' + '/' + 'fifth'

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
        enable_automatic_punctuation=True
    )

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=100000)
    transcript  = []
    for result in response.results:
        transcript.append((result.alternatives[0].transcript))
    transcript = ''.join(transcript)
    print(transcript)
    transcript  = transcript.replace('\n', "")
    sentences = sent_tokenize(transcript)
    transcript = transcript.lower()
    transcript = "".join([char for char in transcript if char not in string.punctuation])
    print(transcript)

    stopWords = set(stopwords.words("english"))
    words = word_tokenize(transcript)
    ps = PorterStemmer()

    freq = {}

    for word in words:
        word = ps.stem(word)
        # print(word)
        if word not in stopWords:
            if word.lower() in freq:
                freq[word] += 1
            else:
                freq[word] = 1
    # print(freq)
    print(sentences)
    sentFreq = {}
    count= 0
    for sent in sentences:
        sentClean = sent.lower()
        sentClean = "".join([char for char in sent if char not in string.punctuation])
        sentWords = word_tokenize(sentClean)
        
        sentWords = (i.lower() for i in sentWords)
        intersection = list(set(sentWords).intersection(set(freq)))
        # print(intersection)

        sentFreq[count] = len(intersection)/len(word_tokenize(sent))
        count += 1
    thresh = sum(sentFreq.values()) / len(sentFreq)

    ret = []
    for sent in sentFreq:
        if sentFreq[sent] > thresh:
            ret.append(sentences[sent])
    #         ret = ret.join(sentences[sent])
    print(' '.join(ret))
    return(' '.join(ret))
    return ''

                    


if __name__ == "__main__":
    app.run()
    # threading.Thread(target=lambda: app.run(debug= True, use_reloader=False)).start()