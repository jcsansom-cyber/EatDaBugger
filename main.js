var canvas = document.getElementById('canvas');
var context = canvas.getContext("2d");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
var player = new Image();
var shot = new Image();
var bug = new Image();
player.src = '/Assets/UFo.png';
shot.src = '/Assets/Shot.png';
var random = Math.random();
if (random < 0.3) {
    bug.src = '/Assets/Bug1.png';
}
else if ( random <0.6) {
    bug.src = '/Assets/Bug2.png'
}
else {
    bug.src = '/Assets/Bug3.png'
}
var score = 0;
var prompt;
var start = false;
var Bullets = 1;
var stars = 5;

window.addEventListener('keydown', function(){
    canvas.key = event.keyCode;
    if(canvas.key == 32) {
        canvas.key=event.keyCode;
        shoot=true;
    }
})

window.addEventListener('keyup', function(){
    canvas.key=false;
})
