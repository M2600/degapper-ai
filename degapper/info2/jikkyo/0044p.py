import sys, io
html1 = '''
<!DOCTYPE html>
<html lang="ja">
    <head><meta charset="UTF-8"></head>'''
html2 = '''
    </body>
</html>'''
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print('Content-Type: text/html; carset=UTF-8\n\n')
print(html1)
print('ここにhtml1とhtml2の間に入れるHTML文を出力する')
print(html)