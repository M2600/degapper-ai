import cgi

def fwrite(data, fn) :
    file = open (fn, mode = 'w', encoding = 'utf-8')
    file.write(data)
    file.close ()
def fread (fn) :
    file = open (fn, mode = 'r', encoding = 'utf-8')
    text = file. readline()
    file.close ( )
    return text

print('Content-Type: text/plain\n')
fsens = 'cgi-bin/sens.txt'
fcont = 'cgi-bin/cont.txt'
param = cgi.FieldStorage()
val = param.getvalue('sens')
if val != None:
    fwrite(val , fsens)
cont = fread(fcont)
print(cont)