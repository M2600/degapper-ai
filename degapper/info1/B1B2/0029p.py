import tkinter
import math
def move() :
    global x, y, vy, t
    canvas.delete('ball')
    canvas.create_oval(x-10, (height-y)-10, x+10, (height-y)+10, fill='red', tags='ball')
    if 0<= x and x <= width and 0<= y and y <= height:
        x = x + vxO * dt
        v1 = vy; v2 = vy -g * dt
        y = y + (v1 + v2)/2.0 * dt
        vy = v2
        t = t + dt
    else:
        x = x0; y = y0; vy = vy0; t= t0
    window.after(50, move)
width = 1000; height = 500
t0 = 0.0; dt = 0.1; g = 9.8
v0 = float(input('初速度を入力してください'))
degrees = float(input('角度を入力してください'))
vxO = v0 * math.cos(degrees * math.pi /180)
vy0 = v0 * math.sin(degrees * math.pi /180)
x0 = width/4; y0 = 3* height/4
x = 10; y = y0; Vy = vy0; t= t0
window = tkinter.Tk()
window.geometry('1020×520')
window.title('動く図形')
canvas = tkinter. Canvas (window, width = 1000, height = 500, bg='white')
canvas.place (x=10, y=10)
canvas.create_oval(x-10,(height-y)-10, x+10, (height-y)+10, fill='red', tags='ball')
move()
window.mainloop()
