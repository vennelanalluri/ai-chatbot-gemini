function newChat(){
 document.getElementById('chatBox').innerHTML='';
}

async function sendMessage(){
 const input=document.getElementById('userInput');
 const msg=input.value.trim();
 if(!msg) return;

 const chat=document.getElementById('chatBox');
 chat.innerHTML += `<div class="user">${msg}</div>`;
 input.value='';

 chat.innerHTML += `<div class="bot" id="typing">Typing...</div>`;

 const res=await fetch('/chat',{
   method:'POST',
   headers:{'Content-Type':'application/json'},
   body:JSON.stringify({message:msg})
 });

 const data=await res.json();

 document.getElementById('typing').remove();
 chat.innerHTML += `<div class="bot">${data.reply}</div>`;
 chat.scrollTop=chat.scrollHeight;
}

document.getElementById('userInput').addEventListener('keypress',e=>{
 if(e.key==='Enter') sendMessage();
});
