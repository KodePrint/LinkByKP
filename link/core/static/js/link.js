var hamburguer = document.querySelector('.btn-hamburguer')
var menu = document.querySelector('.menu')
var collapseBtn = document.querySelector('.collapse-button')

hamburguer.addEventListener('click', () => {
    hamburguer.classList.toggle('open-menu')
    menu.classList.toggle('open-menu')
})

collapseBtn.addEventListener('click', () => {
    menu.classList.toggle('collapse-menu')
})