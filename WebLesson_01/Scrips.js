function drag() {
	mantis = document.getElementById("mantisShrimp");
	leftbox = document.getElementById("leftBox");
	
	mantis.addEventListener("dragstart", startDrag, false);
	mantis.addEventListener("dragend",endDrag, false);
	
	leftbox.addEventListener("dragenter",dragEnter, false);
	leftbox.addEventListener("dragleave", dragLeave, false);
	leftbox.addEventListener("dragover", function(e){e.preventDefault()}, false);
	leftbox.addEventListener("drop", drop, false);
}
function startDrag(e) 
{
	//alert("Works!");
	var pic = '<img id = "mantisShrimp" src = "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQUL_IQahwHxRNKC5RVErAnk-Kh39GC4jkHgMVl5Q0cqyv2H5sZrA">';
	e.dataTransfer.setData('Picture', pic);
}
function dragEnter(e) {
	e.preventDefault();
	leftbox.style.background = "#80657A";
	leftbox.style.border = "3px solid green";
}
function dragLeave(e) {
	e.preventDefault();
	leftbox.style.background = "white";
	leftbox.style.border = "3px solid purple";
}
function drop(e) {
	e.preventDefault();
	leftBox.innerHTML = e.dataTransfer.getData('Picture');
}
function endDrag(e) {
	pic = e.target
	pic.style.visibility = "hidden";
}
window.addEventListener("load", drag, false);
	