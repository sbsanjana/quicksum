import Breadcrumbs from '@mui/material/Breadcrumbs';
import Link from '@mui/material/Link';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';


export default function Nav() {
    return (
<AppBar position="static" style={{backgroundColor:"#FFFCF4", height:70}}>
  <Toolbar variant="dense">
    <IconButton edge="start"aria-label="menu" sx={{ mr: 2 }}>
        QuickSum
    </IconButton>
    <Typography variant="h6"  component="div">
      Photos
    </Typography>
  </Toolbar>
</AppBar>
    );
  }