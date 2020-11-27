from tkinter import *
def tc_calculate():
    cal_1=tvc.get()+tfc.get()
    tc.set(cal_1)

def afc_calculate():
    cal_2=tfc.get()/q.get()
    afc.set(cal_2)

def avc_calculate():
    cal_3=tvc.get()/q.get()
    avc.set(cal_3)

def atc_calculate():
    cal_4=tc.get()/q.get()
    atc.set(cal_4)

def q_calculate():
    cal_6=p.get()-avc.get()
    cal_5=tfc.get()/cal_6
    qb.set(cal_6)

root = Tk()
root.title("Business decisions")
root.configure(width=1200,height=720,bg='#3333CC')
root.iconbitmap(r'mark.ico')
#TC
tc=DoubleVar()
tfc=DoubleVar()
tvc=DoubleVar()
afc=DoubleVar()
avc=DoubleVar()
atc=DoubleVar()
q=DoubleVar()
qb=DoubleVar()
p=DoubleVar()

Label(root, text="The Shot-Run Cost Analysis",font="impact 20",bg='#3333CC').grid(row=0,columnspan=10)
Label(root, text="TC =",font="impact 18",bg='#3333CC').grid(row=1,column=1)
Entry(root, textvariable=tc,width=10).grid(row=1,column=2)
Label(root, text="TFC =",font="impact 18",bg='#3333CC').grid(row=1,column=3)
Entry(root, textvariable=tfc,width=10).grid(row=1,column=4)
Label(root, text="TVC =",font="impact 18",bg='#3333CC').grid(row=1,column=5)
Entry(root, textvariable=tvc,width=10).grid(row=1,column=6)
Button(root, text="TC calculate",command=tc_calculate,bg='#3333CC').grid(row=1,column=7)
#AFC
Label(root, text="AFC =",font="impact 18",bg='#3333CC').grid(row=2,column=1)
Entry(root, textvariable=afc,width=10).grid(row=2,column=2)
Label(root, text="TFC =",font="impact 18",bg='#3333CC').grid(row=2,column=3)
Entry(root, textvariable=tfc,width=10).grid(row=2,column=4)
Label(root, text="Q =",font="impact 18",bg='#3333CC').grid(row=2,column=5)
Entry(root, textvariable=q,width=10).grid(row=2,column=6)
Button(root, text="AFC calculate",command=afc_calculate,bg='#3333CC').grid(row=2,column=7)
#AVC
Label(root, text="AVC =",font="impact 18",bg='#3333CC').grid(row=3,column=1)
Entry(root, textvariable=avc,width=10).grid(row=3,column=2)
Label(root, text="TVC =",font="impact 18",bg='#3333CC').grid(row=3,column=3)
Entry(root, textvariable=tvc,width=10).grid(row=3,column=4)
Label(root, text="Q =",font="impact 18",bg='#3333CC').grid(row=3,column=5)
Entry(root, textvariable=q,width=10).grid(row=3,column=6)
Button(root, text="AVC calculate",command=avc_calculate,bg='#3333CC').grid(row=3,column=7)
#ATC
Label(root, text="ATC =",font="impact 18",bg='#3333CC').grid(row=4,column=1)
Entry(root, textvariable=atc,width=10).grid(row=4,column=2)
Label(root, text="TC =",font="impact 18",bg='#3333CC').grid(row=4,column=3)
Entry(root, textvariable=tc,width=10).grid(row=4,column=4)
Label(root, text="Q =",font="impact 18",bg='#3333CC').grid(row=4,column=5)
Entry(root, textvariable=q,width=10).grid(row=4,column=6)
Button(root, text="ATC calculate",command=atc_calculate,bg='#3333CC').grid(row=4,column=7)
#Q Break even point = tfc/p-avc=tfc/cm
Label(root, text="Q Break even point =",font="impact 18",bg='#3333CC').grid(row=5,column=1)
Entry(root, textvariable=qb,width=10).grid(row=5,column=2)
Label(root, text="TFC =",font="impact 18",bg='#3333CC').grid(row=5,column=3)
Entry(root, textvariable=tfc,width=10).grid(row=5,column=4)
Label(root, text="P =",font="impact 18",bg='#3333CC').grid(row=5,column=5)
Entry(root, textvariable=p,width=10).grid(row=5,column=6)
Label(root, text="AVC =",font="impact 18",bg='#3333CC').grid(row=5,column=7)
Entry(root, textvariable=avc,width=10).grid(row=5,column=8)
Button(root, text="Q calculate",command=q_calculate,bg='#3333CC').grid(row=5,column=9)
root.mainloop()
