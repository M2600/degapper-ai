import cgi
print('Content-Type: text/plain\n')
param = cgi.FieldStorage()
val = param.getvalue('sens')
if int(val) >= 30:
    cont = 'ON'
else:
    cont = 'OFF'
print(cont)