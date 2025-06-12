#!/usr/bin/env python

import dblib
dbc = dblib.DBController()
import util
ut = util.Util()
import cgi

form = cgi. FieldStorage()
next_url = form.getvalue('next_url', '')

template_values = {'next_url': next_url, 'event_name': ''}

event = dbc.get_event()
template_values['event_name'] = event ['event_name']

print('''<!doctype html>
<html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="./asset/css/style.css">
        <title>ログイン - '''+ template_values['event_name'] + '''</title>
    </head>
    <body>
        <header>
            <h1>''' + template_values['event_name'] + ''' / ログイン</h1>
        </header>
        <article id="confirm">
            <form action="''' + template_values['next_url'] + '''" method="post">
                <dl>
                    <dt>メールアドレス</dt>
                    <dd><input type="email" name="mail_address" placeholder="test@example.ed.jp" required></dd>
                    <dt>パスワード</dt>
                    <dd><input type="password" name="password" required></dd>
                </dl>
                <p class="attention">ログインするには、メールアドレスとパスワードを、それぞれ半角文字で入力してください</p>
                <p class="submit"><input type="submit" value="ログイン"></p>
            </form>
        </article>
        <p class="goback"><a href="index.py">TOPに戻る</a></p>
        <footer>
            <address>&copy; ''' + template_values['event_name'] + '''実行委員会</address>
        </footer>
    </body>
</html>
''')