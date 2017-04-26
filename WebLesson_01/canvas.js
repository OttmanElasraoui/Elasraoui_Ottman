function mouse()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	
	window.addEventListener("mousemove", icon, false);
}

function icon(e) {
	canvas.clearRect(0, 0, 600, 600);
	var xPos = e.clientX;
	var yPos = e.clientY;
	var pic = new Image();
	pic.src = "https://img.memesuper.com/2bdbbe42f3fc8c20f7a1d6b389a641d2_-cry-thus-mj-crying-memes_2251-3000.jpeg";
	canvas.drawImage(pic, xPos-50, yPos-50, 100, 100);
}

window.addEventListener("load", mouse, false);
