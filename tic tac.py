from tkinter import *
from tkinter import ttk
from tkinter import messagebox
active_player=1
p1=[]
p2=[]

root = Tk()
root.title('TIC TAC : player 1')
style = ttk.Style()
style.theme_use('classic')

but1 = ttk.Button(root,text=' ')
but1.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40)
but1.config(command=lambda :buclick(1))

but2 = ttk.Button(root,text=' ')
but2.grid(row=0,column=1,sticky='snew',ipadx=40,ipady=40)
but2.config(command=lambda :buclick(2))

but3 = ttk.Button(root,text=' ')
but3.grid(row=0,column=2,sticky='snew',ipadx=40,ipady=40)
but3.config(command=lambda :buclick(3))

but4 = ttk.Button(root,text=' ')
but4.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
but4.config(command=lambda :buclick(4))

but5 = ttk.Button(root,text=' ')
but5.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
but5.config(command=lambda :buclick(5))

but6 = ttk.Button(root,text=' ')
but6.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
but6.config(command=lambda :buclick(6))

but7 = ttk.Button(root,text=' ')
but7.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
but7.config(command=lambda :buclick(7))

but8 = ttk.Button(root,text=' ')
but8.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
but8.config(command=lambda :buclick(8))

but9 = ttk.Button(root,text=' ')
but9.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
but9.config(command=lambda :buclick(9))

def buclick(id):
    global active_player
    global p1
    global p2
    if active_player==1:
        setlayout(id,'X')
        p1.append(id)
        root.title("tic tac:player 2")
        active_player=2
        print("p1:{}".format(p1))
    elif active_player==2:
        setlayout(id,'O')
        p2.append(id)
        root.title("tic tac:player 1")
        active_player=1
        print("p2:{}".format(p2))
    checkwinner()

def setlayout(id,text):
    if id==1:
        but1.config(text=text)
        but1.state(['disabled'])
    elif id==2:
        but2.config(text=text)
        but2.state(['disabled'])
    elif id==3:
        but3.config(text=text)
        but3.state(['disabled'])
    elif id==4:
        but4.config(text=text)
        but4.state(['disabled'])
    elif id==5:
        but5.config(text=text)
        but5.state(['disabled'])

    elif id==6:
        but6.config(text=text)
        but6.state(['disabled'])

    elif id==7:
        but7.config(text=text)
        but7.state(['disabled'])

    elif id==8:
        but8.config(text=text)
        but8.state(['disabled'])
    elif id==9:
        but9.config(text=text)
        but9.state(['disabled'])

def checkwinner():
    winner=-1
    if 1 in p1 and 2 in p1 and 3 in p1:
        winner=1
    if 1 in p2 and 2 in p2 and 3 in p2:
        winner=2

    if 4 in p1 and 5 in p1 and 6 in p1:
        winner=1
    if 4 in p2 and 5 in p2 and 6 in p2:
        winner=2

    if 7 in p1 and 8 in p1 and 9 in p1:
        winner=1
    if 7 in p2 and 8 in p2 and 9 in p2:
        winner=2

    if 1 in p1 and 4 in p1 and 7 in p1:
        winner=1
    if 1 in p2 and 4 in p2 and 7 in p2:
        winner=2

    if 2 in p1 and 5 in p1 and 8 in p1:
        winner=1
    if 2 in p2 and 5 in p2 and 8 in p2:
        winner=2

    if 3 in p1 and 6 in p1 and 9 in p1:
        winner=1
    if 3 in p2 and 6 in p2 and 9 in p2:
        winner=2

    if winner==1:
        messagebox.showinfo(title='winner',message='player 1 is winner')
    if winner == 2:
        messagebox.showinfo(title='winner', message='player 2 is winner')






root.mainloop()