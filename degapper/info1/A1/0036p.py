def func():
    elem = document.querySelector("ol")
    elem.innerHTML += "<li>item</li>"

setInterval(func, 1000)