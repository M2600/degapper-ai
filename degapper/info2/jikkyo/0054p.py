import sqlite3
def display():
    rows = cur.fetchall()
    for row in rows:
        print(row)
名簿 = [('佐藤', 16, '野球'), ('鈴木', 18, '水泳'), ('山下', 17, '演劇')]
sql0 = 'DROP TABLE IF EXISTS 生徒;'
spl1 = 'CREATE TABLE 生徒 (名前 TEXT, 年齢 INTEGER, 部活 TEXT);'
sql2 = 'INSERT INTO 生徒 VALUES (?, ?, ?);'
sql3 = 'SELECT * FROM 生徒;'
com = sqlite3.connect('data.db')
cur = con.cursor()
cur.execute(sqp0)
cur.execute(sql1)
cur.executemany(sql2, 名簿)
cur.commit()
display()
con.close()