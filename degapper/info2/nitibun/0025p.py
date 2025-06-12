#! /usr/bin/env python
import dblib
dbc = dblib.DBController()
import util
ut = util.Util()

program_id = ut.get_uri_parameter('program_id')

template_values = {
    'program_name': '', 'description': '', 'wait_minutes': '',
    'update_time': '', 'program_detail': '',
    'program_id': program_id, 'event_name': ''
}

event = dbc. get_event()
template_values['event_name'] = event['event_name']

if program_id == '':
    template_values['program_name'] = "データを取得できませんでした"
else:
    program = dbc. get_program (program_id)
    if program is None:
        template_values['program_name'] = "データが存在しません"
    else:
        template_values['program_name'] = program['program_name']
        template_values['description'] = program['description']
        template_values['wait_minutes'] = program['wait_time']
        template_values['update_time'] = ut.datetime_to_string(program['update_datetime'])

print('''<!doctype html>
<html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="./asset/css/style.css">
        <title>''' + template_values[ 'program_name'] + '''詳細 -
        ''' + template_values['event_name'] + '''</title>
    </head>
    <body>
        <header>
            <h1>''' + template_values[ 'event_name'] + ''' /
            ''' + template_values[ 'program_name'] + ''' 詳細<h1>
        </header>
        <article id="detail">
            <section>
                <div class="detail_ph">
                    <p><img src="./asset/img/''' +
                    str(template_values['program_id']) + '''-1.jpg"
                    alt="''' + template_values['program_name'] + ''' 詳細画像1"></p>
                    <p><img src="./asset/img/''' +
                    str(template_values['program_id']) + '''-2.jpg"
                    alt=''' + template_values['program_name'] + ''' 詳細画像2"></p>
                </div>
                <h2>''' +  template_values['description'] + '''</h2>
                <p class="time">現在の待ち時間 :
                <span>''' + template_values['wait_minutes'] + '''分</span>
                待ち (''' + template_values['update_time'] + ''' 更新)</p>
            </section>
        </article>
        <p class="goback"><a href="index.py">TOPに戻る</a></p>
        <footer>
            <address>&copy; ''' + template_values['event_name'] + ''' 実行委員会</address>
        </footer>
    </body>
</html>
''')