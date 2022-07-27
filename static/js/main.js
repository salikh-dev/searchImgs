let video = document.querySelectorAll('#vid')
let links = document.querySelectorAll('.links')
video.forEach(function (vid) {
    vid.addEventListener('mouseover', () => {
        vid.play()
    })
    vid.addEventListener('mouseout', () => {
        vid.pause()
    })
})

