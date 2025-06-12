import sys, io, random
html = '''
<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>コイン投げ</title>
    </head>
    <body>
        <h1>コインは{0}です</h1>
    </body>
</html>
'''
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print('Content-Type: text/html; carset=UTF-8\n\n')
if random.randint(0, 1) == 0:
    x = '表'
else:
    x = '裏'
print(html.format(x))