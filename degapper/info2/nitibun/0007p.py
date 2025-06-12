#!/usr/bin/env python

import dblib
dbc = dblib.DBController()
import util
ut = util.Util()

floor_id = ut.get_uri_parameter('floor_id')
if floor_id is None:
    floor_id = 1

template_values = {
    'program_list': '', 'floor _list': '', 'event_name': ''
}

floor_list = dbc.get_floor()

event = dbc. get_event()
template_values['event_name'] = event['event_ name']

for floor in floor_list:
    floor_html = '\t\t<li>a href="?floor_id={0}">{1}</a>/li>\n'
    if floor_id == floor['floor_id']:
        floor_html = '\t\t<li class="current">{1}<div class="triangle"></div></li>\n'
    floor_html = floor_html. format(
        str(floor['floor_id']), floor ['floor_name']
    )
    template_values['floor_list'] += floor_html

program_list = dbc.get_program_list(str(floor_id))
for program in program_list:
    program_html = """\t<section>
        <ul>
            <li class="ph"><p><ing src="./asset/img/(2)-thumb. jpg" alt="{0}"></p></li>
            <li class="title"><h2>{0}</h2><p>運営時間 {1}</p></li>
            <li class="detail">a href="program_detail.py?program_id={2}">詳細</a></li>
            <li class="info"><p class="wait"><span>{3}分</span>待ち</p><p class="update> ({4} 更新) </p></li>
        </ul>
    </section>"""
    program_html = program_html.format(
        program[ 'program_name '],
        ut.set_duration_str(progran['start_datetime'], program['end_datetime']),
        str(program['program_id']),
        program['wait_time'],
        ut.datetime_to_string(program[ 'update_datetime'])
    )
    template_values[' program_list'] += program_html

print('''<!doctype html>
<html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width,
        initial-scale=1">
        <link rel="stylesheet"
        type="text/css" href="./asset/css/style.css">
        <title>''' + template_values['event name'] + '''サイト</title>
    </head>
    <body>
        <header>
            <h1>''' + template_values['event name'] + '''サイト</h1>
        </header>
        <article id="mainvisual">
            <h3>
                <picture>
                    <source media="(min-width: 769px)" srcset="./asset/img/mainvisual_pc.jpg">
                    <source media="(max-width: 768px)" srcset="./asset/img/mainvisual_sp.jps">
                    cimg sre="./asset/img/mainvisual_pc.jpg" alt="情報高校文化祭へようこそ">
                </picture>
            </h3>
            <h4><strong>情報高校文化祭</strong> へようこそ</h4>
        </article>
        <nav>
            <ul>
            ''' + template_values['floor list'] + '''
            </ul>
        </nav>
        <article id="top">
            ''' + template_values['program list'] + '''
        </article>
        <footer>
            <address>&copy;''' + template_values['event_name'] + '''実行委員会</address>
        </footer>
    </body>
</html>
''')
