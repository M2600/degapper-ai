#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import csv
import datetime

import cgitb
cgitb. enable ( )

print('Content-Type:text/html')
print()

form = cgi.FieldStorage()

dtm = datetime.datetime.now()
dtm = dtm.strftime('%Y/%m/%d %H-%M-%S')

with open('board txt', 'a', newline='' ) as f:
	board = csv.writer(f)
	board.writerow([dtm])
	board.writerow([form['name'].value, form['message'].value])

with open('board.txt') as f:
	for display in f:
		display = display.split(',')
		print (':'.join(display))
		print ('<br>')

print("<a href='../clientside.html'><button>投稿画面へ戻る</button></a>")

print ('</body></html>')
