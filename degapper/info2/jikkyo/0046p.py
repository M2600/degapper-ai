import sys, io, random
html1 = '''
<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>加算</title>
    </head>
    <body>
        <form action="calc.py" method="post">
            <p>被加数<br><input type="text" name="num1"></p>
            <p>加数<br><input type="text" name="num2"></p>
            <input type="submit" value="+">
        </form>'''
html2 = '''
    </body>
</html>
'''
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print('Content-Type: text/html; carset=UTF-8\n\n')
print(html1)
form = cgi.FieldStorage()
a = form.getvalue('num1')
b = form.getvalue('num2')
if a != None and b != None:
    c = float(a) + float(b)
    print('<h3>', a, ' + ', b, ' = ', c, '</h3>')
print(html2)