// highlight when running on test site
window.onload = (e) => {
    let re = new RegExp(`^/(test-\\w+)/`)
    let m = location.pathname.match(re)
    if (m) {
        document.querySelector('body').classList.add(m[1])
        let div = document.createElement('div')
        div.classList.add('test-header')
        div.innerText = m[1]
        document.querySelector('body').prepend(div)
    }
}
function fullscreen(img) {
    let d = document.querySelector('.fullscreen')
    if (d) {
        d.remove()
    }
    d = document.createElement('div')
    d.classList.add('fullscreen')
    d.style.backgroundImage = `url(${img.src})`
    d.style.display = 'block'
    document.querySelector('body').append(d)
    d.addEventListener('click', (x) => { 
        d.remove()
    })
}