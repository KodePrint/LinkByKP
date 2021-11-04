var hamburguer = document.querySelector('.btn-hamburguer')
var menu = document.querySelector('.menu')

hamburguer.addEventListener('click', () => {
    hamburguer.classList.toggle('open-menu')
    menu.classList.toggle('open-menu')
})