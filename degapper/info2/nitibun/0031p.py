#! /us/bin/env python
import dblib
dbc = dblib.DBController()
import util
ut = util.Util

program_id = ut. get_uri_parameter('program_id')

wait_time = ut. get_wait_time(program_id)
wait_minutes = ''
for i in range(0, 9):
    value = str(i * 15)
    if wait_time == value:
        wait_minutes += """\t\t\t<option value="{0}" selected>{0}</option>\n""".format(value)
    else:
        wait_minutes += """\t\t\t<option value="{0}">{0}</option>\n""".format(value)

template_values = {
    'program_id': program_id,
    'program_name': ut.get_program_name(program_id),
    'wait_minutes': wait_minutes,
    'event_name': ''
}

event = dbc.get_event()
template_values['event_name'] = event['event_name']
print('''<!doctype html>
<html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="./asset/css/style.css">
        <title>''' + template_values['program_name'] + ''' 待ち時間登録 - ''' + template_values['event_name'] + '''</title>
    </head>
    <body>
        <header>
            <h1>管理画面 / ''' + template_values['program_name '] + ''' 待ち時間登録</h1>
        </header>
        <nav>
            <ul>
                <li class="current">待ち時間登録<div class="triangle"></div></li>
            </ul>
        </nav>
        <article id="admin_cont">
            <form action="update_wait_time.py" method="post">
                <input type="hidden" name="program_id" value="''' + str(template_values['program_id']) + '''">
                <p class="time">現在の待ち時間:
                <select name="wait_minutes">''' + template_values['wait_minutes'] + ''' </select> 分</p>
                <p class="submit"><input type="submit" value="登録"></p>
            </form>
        </article>
        < footer>
            <address>&copy; ''' + template_values[' event_name '] + '''実行委員会</address>
        </footer>
    </body>
</html>
''')