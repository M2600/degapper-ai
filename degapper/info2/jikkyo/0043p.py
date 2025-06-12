import sys, io
html = '''
<!DOCTYPE html>
<html lang="ja">
    <head><meta charset="UTF-8"></head>
    <body>
        {}が埋め込まれたHTML文の一部分
    </body>
</html>
'''
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print('Content-Type: text/html; carset=UTF-8\n\n')
変数 = 'プログラムで計算した値'
print(html.format(変数))