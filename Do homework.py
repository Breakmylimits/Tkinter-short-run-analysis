from tkinter import *
from datetime import datetime
from tkinter import Tk
from typing import TextIO
from tkinter import messagebox
from subprocess import call

def member(e):
    global root
    root.destroy()
    r=Tk()
    r.title("Business decisions")
    r.option_add("*Font", "impact 15")
    r.configure(bg='#3333CC')
    f_name=StringVar()
    l_name=StringVar()
    pas=StringVar()

    def mem(e):
        with open("member.csv", mode='a', newline='', encoding='UTF-8')as f:
            f1=f_name.get()
            f2=l_name.get()
            f3=pas.get()
            f.write(f'ผู้ใช้ : {f1}\n,รหัส :{f2}\n,หัส :{f3}\n')
            messagebox.showinfo('แจ้งเตือน', 'ทำการลงทะเบียนเรียบร้อยแล้ว')
    Label(r, text="ลงทะเบียน",bg='#3333CC').grid(row=0,columnspan=10)
    Label(r, text="ชื่อ :",bg='#3333CC').grid(row=1,column=0,padx=20)
    Entry(r, textvariable=f_name).grid(row=1,column=1)
    Label(r, text="สกุล :",bg='#3333CC').grid(row=1,column=2,padx=20)
    Entry(r, textvariable=l_name).grid(row=1,column=3,padx=20)
    Label(r, text="รหัส :",bg='#3333CC').grid(row=2,column=0,padx=20,pady=10)
    Entry(r, textvariable=pas).grid(row=2,column=1,pady=10)
    Btn_mem = Button(r, text="ลงทะเบียน",bg='#3333CC')
    Btn_mem.grid(row=2, column=2,padx=10)
    Btn_mem.bind("<Button-1>", mem)
    r.iconbitmap(r'mark.ico')
    r.mainloop()




def set(e):
    global root

    with open("Log.csv", mode='a', newline='', encoding='UTF-8')as f:
       u=User.get()
       p1=p.get()
       dt = datetime.now().strftime("%Y-%d-%m-%H:%M:%S")
       f.write(f'ผู้ใช้ : {u}\n,รหัส :{p1}\n,เวลาเข้าใช้{dt}\n')
    messagebox.showinfo('แจ้งเตือน', 'ชื่อคุณถูกบันทึกแล้ว')
    root.destroy()
    call(["python", "The Shot-Run Cost Analysis.py"])



root = Tk()
root.title("Business decisions")
root.option_add("*Font", "impact 15")
root.configure(bg='#3333CC')
root.iconbitmap(r'mark.ico')

User = StringVar()
p = StringVar()
u = StringVar()
p1 = StringVar()

Label(root, text="ชื่อผู้ใช้",bg='#3333CC').grid(row=0, column=0)
Entry(root, textvariable=User).grid(row=0, column=1)
Label(root, text="รหัส", justify=RIGHT,bg='#3333CC').grid(row=1, column=0)
Entry(root, textvariable=p ).grid(row=1, column=1)

Btn_log = Button(root, text="เข้าใช้",bg='#3333CC')
Btn_log.grid(row=2, column=0)
Btn_log.bind("<Button-1>",set)
Btn_mem=Button(root, text="ลงทะเบียน",bg='#3333CC')
Btn_mem.grid(row=2, column=1,sticky="news")
Btn_mem.bind("<Button-1>", member)
root.mainloop()
