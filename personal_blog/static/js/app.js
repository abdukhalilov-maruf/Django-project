
const typeMe = document.querySelector(".btn--red")
const modalClose = document.querySelector('.modal_close')
const contactModal = document.querySelector('.modal')

typeMe.addEventListener('click', function(){
    contactModal.classList.add('show')
})

modalClose.addEventListener('click', function(){
    contactModal.classList.remove('show')
})