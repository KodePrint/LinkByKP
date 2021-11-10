var hamburguer = document.querySelector('.hamburger-menu')
var menu = document.querySelector('.menu')
var content = document.querySelector('.main')
var collapseBtn = document.querySelector('.collapse-button')
var barState = localStorage.getItem('bar')


hamburguer.addEventListener('click', () => {
    hamburguer.classList.toggle('open-menu')
    document.querySelector('.menu').classList.toggle('open-menu')
})

if (barState == 'collapse') {
    menu.classList.add('collapse-menu')
    content.classList.add('collapse-menu')
} else {
    menu.classList.remove('collapse-menu')
    content.classList.remove('collapse-menu')

}

collapseBtn.addEventListener('click', () => {
    let state
    menu.classList.toggle('collapse-menu')
    content.classList.toggle('collapse-menu')
    state = menu.classList.contains('collapse-menu') ? 'collapse' : 'expanded'
    localStorage.setItem('bar', state)
})