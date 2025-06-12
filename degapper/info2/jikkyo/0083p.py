import cgi, sys, io, os, datetime

def InputData() :
    filename = 'cgi-bin/bbs.txt'
    d = datetime.datetime.now()
    t = d.strftime ('%Y/%m/%d %H:%M:%S')
    ip = os.environ.get('REMOTE_ADDR')
    form = cgi.FieldStorage()
    name = form.getvalue('na')
    message = form.getvalue('msg')
    if message is not None:
        words = message.replace('\r\n', '<br>').replace('\r', '<br>'). replace('\n', '<br>')
        data = t + '‹br›' + ip + '‹br›' + name + '‹br›' + words + '<hr>\n'
        file = open(filename, mode='a', encoding='utf-8')
        file.write(data)
        file.close()

def OutputData():
    filename = 'cgi-bin/bbs.txt'
    if os.path.exists(filename) == True:
        file = open(filename, mode='r', encoding='utf-8')
        text = file.readlines()
        file.close()
        text.reverse()
        for line in text:
            print(line)

html1 = '''
<! DOCTYPE html>
<html lang = "ja">
    <head>
        <meta charset = "UTF-8">
        <title> flamir</title>
    </head>
    <body>
        <form method="post" action="bbs.py">
        <p>名前<br><input name="na" type="text" style="width:120px"></p>
        <p>発言<br><textarea name="msg" rows="4" cols="40"></textarea></p>
        <p><input type="submit" value="送信する"></р>
        </form>
'''
html2 = '''
    </body>
</html>
'''