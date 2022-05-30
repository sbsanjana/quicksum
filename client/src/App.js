import work from './work.svg';
import Header from './components/Header'
import Grid from '@mui/material/Grid';
import Nav from './components/Nav'
import './App.css';
import Button from '@mui/material/Button';
import FileUpload from './components/FileUpload';
function App() {
  return (
    <div className="App"  >
      <Grid
        style={{padding:30}}
        container
        item
        direction="row"
        justifyContent="flex-end"
        alignItems="center">      
            <Nav /> 
      </Grid>


      <div style={{padding:150}}>
      <Grid container direction="row">
      

        <Grid container direction="column" item sm={6}>
        <Grid
        container
        item
        direction="row"
        alignItems="flex-start">
          <Header />
      </Grid>

      <Grid container direction="column" item sm={6}>
        <Grid
        container
        item
        direction="row"
        alignItems="flex-start">
          <FileUpload />
          
      </Grid>



        </Grid>

        <Grid container direction="column" item sm={6} >
        <img
        src={work}
        style={{height:"95%", width:"95%"}}
        loading="lazy"
      />
          
        </Grid>

      </Grid>
      </Grid>
      </div>
      

      
      
    </div>
  );
}

export default App;
