const {ipcRenderer} = require('electron'); // there is a "remote" module provided that reduces the amount of usage of ipcrenderer and ipcmain again and again
const button1 = document.getElementById('btn');
const close_btn=document.getElementById('close-tracy');
let A;
function animate(A){
  let out2 = document.getElementById('inp');
  out2.textContent = A;

  // Reset the animation by removing the class and adding it again
  out2.classList.remove('fade-in-text');
  void out2.offsetWidth; // Trigger a reflow to apply the class removal immediately
  out2.classList.add('fade-in-text');
}

close_btn.addEventListener('click',()=>{
  ipcRenderer.send('close-exe');
});

button1.addEventListener('mouseover', () => {
  button1.style.cursor = 'pointer';
    button1.style.backgroundColor='white';
});
button1.addEventListener('mouseout', () => {
  button1.style.cursor = 'default';
  button1.style.backgroundColor='bisque';
});
button1.addEventListener('click',()=>{
    if(button1.style.borderColor="black"){
      button1.style.borderColor="pink";
    }
    
    
    ipcRenderer.send('start-tracy');
});
// ipcRenderer.on('close-exe-msg',(event,data)=>{
//   let out2=document.getElementById('inp');
//   out2.val=data;
// })
ipcRenderer.on('output',(event,data)=>{
    // let out = document.getElementById('inp');
    // out.textContent=data;
    animate(data)
});
ipcRenderer.on('terminated',(event,data)=>{
  // let out2=document.getElementById('inp');
  // out2.textContentn="Tracy Terminated!";
  animate("Tracy Terminated!");
});