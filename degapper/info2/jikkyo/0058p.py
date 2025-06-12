v = document.getElementById('vd')
c = document.getElementById('cv')
fps = 30
tx = [
    [1.0, 2.5, 50, 150, '#FFAA00', '川越の紹介。'],
    [3.2, 6.2, 20, 400, '#FFFF00', 'この建物は時の鐘といいます。'],
    [3.2, 6.2, 20, 400, '#FFFF00', '川越市のシンボル的な建物です・'],
    [8.1, 11.4, 10, 450, '#00FFFF', '蔵造りの町並みが続いています。'],
]
ctx = c.getContent('2d')
ctx.font = '40px sans-font'
ctx.strokeStyle = '#FF0000'
ctx.lineWidth = 5
setInterval(show, 1000 / fps)