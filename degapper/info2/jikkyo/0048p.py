import cgi, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print('Content-Type: text/html; charset=utf-8\n\n')
form = cgi.FieldStorage()
a = form.getvalue('num1')
b = form.getvalue('num2')
if a != None and b != None:
    c = float(a) + float(b)
    print(a, ' + ', b, ' = ', c)