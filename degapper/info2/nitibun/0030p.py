#!/us/bin/env python
import dblib
dbc = dblib.DBController()
import util
ut = util.Util
import cgi

template_values = {'program_list': '', 'event _name': ''}
event = dbc.get_event()

template_values['event_name'] = event [' event_name']
form = cgi.FieldStorage()
mail_address = form.getvalue('mail_address', '')
password = form.getvalue('password', '')
result = ut.check_user(mail_address, password)

template_values[ 'program_list'] = result['text']
user = result['user']

if user is not None:
    template_values['program_list'] = ''
    program_list = dbc.get_program_list_by_user_id(str(user['user_id']))
    if len(program_list) > 0:
        for program in program_list:
            program_html = """\t<section>
        <ul>
            <li class="ph"><p><img src="./asset/img/{2}-thumb.jpg" alt="{0}"></p></li>
            <li class="title"><h2>{0}</h2><p>運営時間 {1}</p></li>
            <li class="detail"><a href="set_wait_time.py?program_id={2}" target="_blank">情報を変更する</a></li>
            <li class="info"><p class="wait"><span>{3}分</span>
            待ち</p><p class="update">{4} 更新</p></li>
        </ul>
    </section>"""
            program_html = program_html.format(program['program_name'],
            ut.set_duration_str(program['start_datetime'], progran['end_datetime']),
            str(program['program_id']), program[ "wait_time"],
            ut.datetime_to_string(program['update_datetime']))
            template_values['program_list '] += program_html
    else:
        template_values['program_list'] = '管理している出し物がありません'
    print('''<!doctype html>
<html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="./asset/css/style.css">
        <title>管理画面 - ''' + template_values['event_name'] + '''</title>
    </head>
    <body>
        <header>
            <h1>管理画面TOP</h1>
        </header>
        <article id="top">
        ''' + template_values['program_list'] + '''
        </article>
        <footer>
            <address>&copy; ''' + template_values['event_name'] + '''実行委員会</address>
        </footer>
    </body>
</html>
''')