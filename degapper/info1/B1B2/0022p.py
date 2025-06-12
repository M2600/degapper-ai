import tkinter as tk
import tkinter.filedialog as fd
def btn1Click() :
    global file
    txtbox2. delete('1.0', 'end')
    fTyp =[('CSVファイル','.csv')]
    iDir = './'
    file = fd.askopenfilename(filetypes = fTyp, initialdir = iDir)
def btn2Click() :
    t1 = txtbox1.get ()
    txtbox2.delete ('1.0', 'end')
    txtbox2.insert('end', '' + t1 + '℃以上' + '¥n')
    fp = open(file, 'rt')
    for b in fp:
        a = b.split(',')
        date = a[0]
        t2 = a[1]
        if float(t2) >= float(t1):
            txtbox2. insert('end', '' + date + ' : ' + t2 + '¥n')
    fp.close()
file = ''
window = tk.Tk()
window.geometry('300x200')
window.title('最高気温の検索')
btn1 = tk.Button(text = 'ファイル選択', command = btn1Click)
btn1.place(x=40, y=20, width=70, height=20)
txtbox1 = tk.Entry()
txtbox1.place(x=40, y=60, width=70, height=20)
btn2 = tk.Button(text = '表示', command = btn2Click)
btn2.place (x=40, y=100, width=70, height=20)
txtbox2 = tk.Text()
txtbox2.place(x=150, y=0, width=150, height=200) 
txtbox1.focus_set()
window.mainloop ()