var canvas = document.getElementById('canvas');
var context = canvas.getContext("2d");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
var player = new Image();
var shot = new Image();
var bug = new Image();
player.src = '/Assets/UFo.png';
shot.src = '/Assets/Shot.png';
var dead = false;
var star = 5;
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
var counter = 0;
var shoot = false;
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

function piece(img, x, y, width, height, isBull, isPlay, isBug, color, dx, dy) {
    this.img = img;
    this.x = x;
    this.y = y;
    this.width = width;
    this.height = height;
    this.color = color;
    this.dx = dx;
    this.dy = dy;
    this.radius =20;
    this.draw=function() {
        context.drawImage(this.img, thistory.x, this.y, this.width, this.height);
    }
    this.collisionplayer=function() {
        if((this.x) < (player.x + player.width) && (this.y) < (player.y + player.height)) {
            console.log("GO");
            dead = true;
            context.font="30px Arial";
            context.fillText("Game Over", innerWidth, innerHeight/2);
            playAgain("play Again? y/n");
        }
    }
    this.collision=function() {
        if ((this.x) < (bullet.x + bullet.width) && (this.y) < (bullet.y + bullet.height) && this.x > bullet.x && this.y > bullet.y) {
            score += 1;
            this.width = 0;
            this.x =0;
            this.y=0;
            this.dx=0;
            this.dy=0;
            thistory.height=0;
        }  
    }
    this.update = function () {
        if(isBullet) {
            if (canvas.key && canvas.key === 32) {
                bullet.y = player.y;
                bullet.x = player.x;
            }
        bullet.y -= 20;
        this.draw();
            
        } else if (isShip) {
            if(this.x >= innerWidth - this.width - 5 || this.x <= 0) {
                this.x = -this.x;
            }
            if(this.y >= innerHeight - this.height - 5 || this.y <= 0) {
                this.y = -this.y;
            }
            if(canvas.key && canvas.key == 37) {
                this.x -= 5;
            } else if (canvas.key && canvas.key == 39) {
                this.x += 5;
            } else if (canvas.key && canvas.key == 38) {
                this.y -= 5;
            } else if (canvas.key && canvas.key == 40) {
                this.y += 5;
            }
            this.draw();
        } else if (isComet) {
            if ((this.x + this.radius > innerWidth) || (this.x - this.radius) < 0) {
                this.dx = -this.dx;
            } else if ((this.y + this.radius > innerHeight) || (this.y - this.radius) < 0) {
                this.dy = -this.dy;
            }
            this.x += this.dx;
            this.y += this.dy;
            this.collisionplayer();
            this.draw();
        }
    }
}
var player = new piece(player, innerWidth/2, innerHeight/2, 100, 50, false, true, false);
var bullet = new piece(shot, Math.random() * innerWidth, Math.random() * (innerHeight - 110),100, 50, true,false,false );
var starArrays = [];
var bulletArrays = [];
for (var i=0; i<Bullets; i++) {
    bulletArrays.push(bullet);
} 
for (var i =0; i< stars; i++) {
    var dx = Math.random()*2;
    var dy = Math.random()*2;
    var starx = Math.random() * innerWidth;
    var stary = Math.random() * innerHeight;
    starArrays.push(new piece(bug, 50+20, 30, 75, 75, false, false, true, "red", dx, dy));
}
function startGame() {
    var input = prompt("Start Game: y/n");
    if (input === 'y' || input === "Y") {
        start = true;
    }
    animate();
}

function playAgain(str) {
    if (dead == true) {
        prompt = prompt(str);
        if (prompt == 'y' || prompt == "Y") {
            location.reload;
        }
    }
}

function animate() {
    if (start) {
        playAgain("Play Again? Y/N");
        requestAnimationFrame(animate);
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.font = "30px Arial";
        ctx.fillStyle = "#69008C"
        ctx.fillText("Score: " + score, 10, 50)
        for (var i = 0; i < starArrays.length; i++) {
            starArrays[i].update();
            starArrays[i].collision(starArrays[i]);
        }
        for (var b = 0; b < bulletArrays.length; b++) {
            if (shoot) {
                bulletArrays[b].update();
                bulletArrays[b].collision();
            }
        }
        player.update();
    }
}
