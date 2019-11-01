const toTop = document.querySelector('.to-top')
toTop.style.opacity = 0
toTop.disabled = true
window.addEventListener('scroll', () => {
    if(window.scrollY >= 200) {
        toTop.style.opacity = 1
        toTop.disabled = false
        toTop.style.cursor = "pointer"
    }
    else if(window.scrollY < 200) {
        toTop.style.opacity = 0 
        toTop.style.transition = ".5s"
        toTop.style.cursor = "default"
        toTop.disabled = true
    }
})
toTop.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        left: 0,
        behavior: "smooth"
    })
})