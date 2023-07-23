const {app, BrowserWindow, Menu, ipcMain, Tray} = require("electron");
const path = require('path');
const { spawn } = require('child_process'); // for using .exe file, and displaying the output text that comes in cmd.
const { exec } = require('child_process');
let child;
let win = null; 

app.whenReady().then(()=> {
    tray = new Tray('./assets/icon.ico');
    win = new BrowserWindow({
        width: 800,
        height: 600,
        icon: path.join(__dirname, './assets/icon.ico'),
        resizable: false,
        webPreferences: {
            nodeIntegration: true, // Integrating node to electron 
            contextIsolation: false,
        }
    })
    win.on('minimize',()=>{
        win.hide();
    });
    tray.on('click',()=>{
        win.show();
    })
    win.loadFile("index.html")
    win.on('closed',()=>{
        tray.destroy();
        tray=null;
        win=null;
    })
});


ipcMain.on('start-tracy',(event)=>{
    const exepath = 'G:\\Development_Training\\Electron\\exe_file\\Tracy.exe';
    child = spawn(exepath);
    
    child.stdout.on('data',(data)=>{
        win.webContents.send('output',data.toString());
    });
    child.stderr.on('data',(data)=>{
        console.error(`=> ${data}`);
    });
    child.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
    });
});
ipcMain.on('close-exe',(event)=>{
    const process = 'Tracy.exe';
    exec(`taskkill /f /im ${process}`, (error, stdout, stderr) => {
        if (error) {
          console.error(`Error executing taskkill: ${error}`);
          return;
        }
        console.log(`stdout: ${stdout}`);
        console.error(`stderr: ${stderr}`);
      });
      win.webContents.send('terminated');
    
});

