import * as React from 'react';
import { styled } from '@mui/material/styles';
import Button from '@mui/material/Button';


export default function FileUpload(props) {
    const handlefileupload = (e) => {
        if (!e.target.files) {
          return;
        }
        const file = e.target.files[0];
        const { name } = file;
        const formData = new FormData();
        formData.append('inputFile', file);
        console.log(file);
        fetch('http://127.0.0.1:5000/upload', {
            method: 'POST',
            body: formData,
        });
    }
  return (
  
    <Button
    variant="contained"
    component="label"
    style={{backgroundColor:"#aa3971"}}
    size="large"
  >
    Try It Now
    <input
      type="file"
      hidden
      onChange={handlefileupload}
    />
  </Button>
  );
}