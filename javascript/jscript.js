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
  modalImg.src = "imagenes/tutorial.png";
var span = document.getElementsByClassName("close")[0];
span.onclick = function() {
  modal.style.display = "none";
}
}
const cdm = document.getElementById('bdm');

const currentTheme = localStorage.getItem("theme");

tema = document.getElementById('theme')

if (currentTheme == "dark") {
  tema.innerHTML = 'dark'
  document.body.classList.toggle('dark');
  document.querySelector(".plots").classList.toggle("darkplots");
  document.querySelector(".oldb").classList.toggle("darkbotones");
  document.querySelector(".oldb2").classList.toggle("darkbotones");
}

cdm.addEventListener('click', function handleClick() {
  if (tema.innerHTML=='dark'){
    tema.innerHTML='light'
  }else{
    tema.innerHTML='dark'
  }
  document.body.classList.toggle('dark');
  document.querySelector(".plots").classList.toggle("darkplots");
  document.querySelector(".oldb").classList.toggle("darkbotones");
  document.querySelector(".oldb2").classList.toggle("darkbotones");
  let theme = "light";
  if (document.body.classList.contains("dark")) {
    theme = "dark";
  }
  localStorage.setItem("theme", theme);
});