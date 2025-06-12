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