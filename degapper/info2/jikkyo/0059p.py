def show():
    ctx.drawImage(v, 0, 0, 640, 480, 0, 0, 640, 480)
    now = v.currentTime
    for i in range(len(tx)):
        start = tx[i][0]
        end = tx[i][1]
        x = tx[i][2]
        y = tx[i][3]
        col = tx[i][4]
        txt = tx[i][5]
        if start <= now and now <= end:
            ctx.fillStyle = col
            ctx.strokeText(txt, x, y)
            ctx.fillText(txt, x, y)

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