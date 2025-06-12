import cgi, sys, io, os, datetime, sqlite3

def InputData() :
    filename = 'cgi-bin/bbs.db'
    d = datetime.datetime.now()
    t = d.strftime ('%Y/%m/%d %H:%M:%S' )
    ip = os.environ.get ('REMOTE_ADDR')
    form = cgi.FieldStorage()
    name = form.getfirst('na')
    message = form.getfirst('msg')
    if message is not None:
        words = message.replace(('\r\n' or '\r' or '\n'), '‹br>')
        con = sqlite3.connect(filename)
        cursor = con.cursor
        sql1 = '''
        CREATE TABLE IF NOT EXISTS
        bbstable(id INTEGER PRIMARY KEY AUTOINCREMENT,
        t TEXT, ip TEXT, name TEXT, words TEXT);
        '''
        sql2 = '''
        INSERT INTO
        bbstable (t,ip,name,words) VALUES(?,?,?,?);
        '''
        data = (t, ip, name, words)
        cursor.execute(sql1)
        cursor.execute (sql2,data)
        con.commit()
        con.close()

def OutputData():
    filename = 'cgi-bin/bbs.db'
    if os-path.exists (filename) == True:
        con = sqlite3.connect(filename)
        cursor = con.cursor()
        sql3 = 'SELECT * FROM bbstable;'
        cursor.execute(sql3)
        rows = cursor.fetchall()
        con.commit()
        con.close()
        if rows is not None:
            rows.reverse()
            for row in rows:
                if row[3] is not None and row[4] is not None:
                    for i in range (1,5):
                        print (row[i], '<br>')
                        print ('<hr>')