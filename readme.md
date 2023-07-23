# Using ipc module to make events occur in main js


1. first __require__ the ipc module from the 'electron'
2. then generate an event in render.js  (for ex. ipc.send('click button');)
3. In the main.js file we catch that event using ipc.on('click button');
4. We can even send a reply to the event that the event have successfully completed or started.