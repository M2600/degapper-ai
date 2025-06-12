#!/usr/bin/env python

import dblib
dbc = dblib.DBController()
import util
ut = util.Util()
import cgi

form = cgi.FieldStorage()
program_id = form. getvalue('program_id', '')
wait_minutes = form. getvalue('wait_minutes', '')

template_values = {
    'message': '待ち時間を登録しました',
    'event_name': '',
    'program_name': '',
    'program_id': program_id
}

template_values['program_name'] = ut.get_program_name(program_id)

event = dbc.get_event()
template_values['event_name'] = event['event_name']

dbc. update_wait_time(program_id, wait_minutes)

print('''<!doctype html>
<html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="./asset/css/style.css">
        <title>''' + template_values['program_name'] + ''' 待ち時間登録- '''+
        template_values['event_name'] + '''</title>
    </head>
    <body>
        <header>
            <h1>管理画面 / '''+ template_values['program_name'] + ''' 待ち時間登録</h1>
        </header>
        <p class="message">''' + template_values['message'] + '''</p>
        <p class="goback"><a href="set_wait_time.py?program_id=''' + str(template_values[ 'program_id']) + '''">前に戻る</a></p>
        <footer>
            <address>&copy; ''' + template_values['event_name'] + '''実行委員会</address>
        </footer>
    </body>
</html>
''')