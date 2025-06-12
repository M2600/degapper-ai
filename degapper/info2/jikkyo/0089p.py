import cgi, sys, io

def fwrite(data, fn) :
    file = open(fn, mode = 'w', encoding = 'utf-8')
    file.write (data)
    file.close()

def fread(fn):
    file = open(fn, mode = 'r', encoding = 'utf-8')
    text = file. readline()
    file.close()
    return text

html = '''
<! DOCTYPE html>
<html lang = "ja">
    <head>
        <meta charset = "UTF-8">
        <title>IoTORk<</title>
    </head>
    <body>
        <h2> 温度 : {0}°C
        <input type = "button" value = "更新" onclick = "window.location.reload();">
        <form action="index-py" method="post">
            LED :
            <input type = "submit" name = "btnl" value = "ON">
            <input type = "submit" name = "btn2" value = "OFF">
        </form>
        </h2>
    </body>
</html>
'''

sys.stdout = io.TextIOWrapper(sys. stdout.buffer, encoding = 'utf-8')
print('Content-Type: text/html; charset = utf-8\n\n')
fsens = 'cgi-bin/sens.txt'
fcont = 'cgi-bin/cont.txt'
form = cgi.FieldStorage()
if form.getvalue('btn1') == 'ON' :
    fwrite('ON', fcont)
elif form.getvalue('btn2') == 'OFF' :
    fwrite( 'OFF' , fcont)
val = fread(fsens)
print(html.format(val))