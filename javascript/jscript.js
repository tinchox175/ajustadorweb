const container = document.getElementById('plot');

const tuto = document.getElementById('content');

const btn = document.getElementById('btn');

btn.addEventListener('click', function handleClick() {
  container.replaceChildren();
});
const graficoold = document.getElementById('plot');

const regraficar = document.getElementById('yo');

regraficar.addEventListener('click', function handleClick() {
  graficoold.replaceChildren();
});
document.getElementById('myfile').onchange = function() {
  tuto.replaceChildren();
}
var modal = document.getElementById("hint");
var img = document.getElementById("hintB");
var modalImg = document.getElementById("tutorialP");
img.onclick = function(){
  modal.style.display = "block";
  modalImg.src = "tutorial.png";
var span = document.getElementsByClassName("close")[0];
span.onclick = function() {
  modal.style.display = "none";
}
}
