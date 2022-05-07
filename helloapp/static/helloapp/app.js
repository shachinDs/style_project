let glc=document.querySelector('#get-location');
let sl=document.querySelector('#send-your-current-location');
let sa=document.querySelector('#show-people');
let time=()=>{
    setTimeout(()=>{
        sl.style.display='inline';
    },1000)
}
glc.addEventListener('click',time);
console.log('sdfa')