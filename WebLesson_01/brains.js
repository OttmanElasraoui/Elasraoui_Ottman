function shapes()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	canvas.strokeStyle = "yellow";
	canvas.fillStyle = "purple";
	canvas.beginPath();
	canvas.moveTo(50, 50);
	canvas.lineTo(70, 250);
	canvas.lineTo(300, 200);
	canvas.lineTo(100, 150);
	canvas.lineTo(700, 200);
	canvas.lineTo(75, 61);
	canvas.lineTo(100, 993);
	canvas.lineTo(33, 175);
	canvas.lineTo(59, 200);
	canvas.lineTo(339, 776);
	canvas.lineTo(234, 432);
	canvas.lineTo(729, 492);
	canvas.lineTo(819, 194);
	canvas.lineTo(392, 381);
	canvas.lineTo(919, 200);
	canvas.lineTo(183, 381);
	canvas.lineTo(915, 382);
	canvas.lineTo(529, 721);
	canvas.lineTo(481, 172);
	canvas.lineTo(628, 322);
	canvas.lineTo(712, 212);
	canvas.lineTo(666, 777);
	canvas.lineTo(131, 265);
	canvas.lineTo(355, 888);
	canvas.lineTo(616, 212);
	canvas.lineTo(414, 111);
	canvas.lineTo(555, 818);
	canvas.closePath();
	canvas.stroke();
	canvas.fill();
}

window.addEventListener("load", shapes, false);
	