var hamburguer = document.querySelector('.btn-hamburguer')
var menu = document.querySelector('.menu')
var collapseBtn = document.querySelector('.collapse-button')
var barState = localStorage.getItem('bar')

hamburguer.addEventListener('click', () => {
    hamburguer.classList.toggle('open-menu')
    menu.classList.toggle('open-menu')
})

if (barState == 'collapse') {
    menu.classList.add('collapse-menu')
} else {
    menu.classList.remove('collapse-menu')

}

collapseBtn.addEventListener('click', () => {
    let state
    menu.classList.toggle('collapse-menu')
    state = menu.classList.contains('collapse-menu') ? 'collapse' : 'expanded'
    localStorage.setItem('bar', state)
})