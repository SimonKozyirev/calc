from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import *
from random import *

root = Tk()
root.title("калькулятор")
root.geometry("400x300")
root.resizable(False, False)


def button1_clicked(*event):
    if len(e['text']) < 14:
        e['text'] += '1'


def button2_clicked(*event):
    if len(e['text']) < 14:
        e['text'] += '2'


def button3_clicked(*event):
    if len(e['text']) < 14:
        e['text'] += '3'


def button4_clicked(*event):
    if len(e['text']) < 14:
        e['text'] += '4'


def button5_clicked(*event):
    if len(e['text']) < 14:
        e['text'] += '5'


def button6_clicked(*event):
    if len(e['text']) < 14:
        e['text'] += '6'


def button7_clicked(*event):
    if len(e['text']) < 14:
        e['text'] += '7'


def button8_clicked(*event):
    if len(e['text']) < 14:
        e['text'] += '8'


def button9_clicked(*event):
    if len(e['text']) < 14:
        e['text'] += '9'


def button0_clicked(*event):
    if len(e['text']) < 14:
        e['text'] += '0'


def buttonc_clicked(*event):
    try:
        if state.get() == "div":
            answer = str(int(e1['text']) // int(e2['text']))
        else:
            answer = str(int(e1['text']) % int(e2['text']))

    except:
        answer = "некорректные данные"
    showinfo(title="Ответ", message=answer)


def buttond_clicked(*event):
    e['text'] = e['text'][:-1]


def buttone_clicked(*enter):
    global e
    e['background'] = "#C0C0C0"
    if e == e2:
        e = e1
    else:
        e = e2
    e['background'] = "yellow"


e1 = ttk.Label(background="yellow", foreground="#800000", width=15, padding=10, borderwidth=2, relief="ridge")
e1.configure(text="")
e2 = ttk.Label(background="#C0C0C0", foreground="#800000", width=15, padding=10, borderwidth=2, relief="ridge")
e2.configure(text="")

e = e1
for i in range(3): root.columnconfigure(index=i, weight=1)
for j in range(7): root.rowconfigure(index=j, weight=1)

btn1 = Button(text='1', command=button1_clicked)
root.bind("1", button1_clicked)
btn1.grid(row=2, column=0)

btn2 = Button(text='2', command=button2_clicked)
root.bind("2", button2_clicked)
btn2.grid(row=2, column=1)

btn3 = Button(text='3', command=button3_clicked)
root.bind("3", button3_clicked)
btn3.grid(row=2, column=2)

btn4 = Button(text='4', command=button4_clicked)
root.bind("4", button4_clicked)
btn4.grid(row=3, column=0)

btn5 = Button(text='5', command=button5_clicked)
root.bind("5", button5_clicked)
btn5.grid(row=3, column=1)

btn6 = Button(text='6', command=button6_clicked)
root.bind("6", button6_clicked)
btn6.grid(row=3, column=2)

btn7 = Button(text='7', command=button7_clicked)
root.bind("7", button7_clicked)
btn7.grid(row=4, column=0)

btn8 = Button(text='8', command=button8_clicked)
root.bind("8", button8_clicked)
btn8.grid(row=4, column=1)

btn9 = Button(text='9', command=button9_clicked)
root.bind("9", button9_clicked)
btn9.grid(row=4, column=2)

btn0 = Button(text='0', command=button0_clicked)
root.bind("0", button0_clicked)
btn0.grid(row=5, column=1)

btnc = Button(text='Count', command=buttonc_clicked)
root.bind("<Alt_L>", buttone_clicked)
btnc.grid(row=6, column=2)

btnd = Button(text='Delete', command=buttond_clicked)
root.bind("<BackSpace>", buttond_clicked)
btnd.grid(row=5, column=0)

btne = Button(text='->', command=buttone_clicked)
root.bind("<Alt_L>", buttone_clicked)
btne.grid(row=5, column=2)

state = StringVar(value="div")

l = ttk.Radiobutton(text="div", value="div", variable=state)
l.grid(row=1, column=0)

r = ttk.Radiobutton(text="mod", value="mod", variable=state)
r.grid(row=1, column=2)

e1.grid(row=0, column=0)
e2.grid(row=0, column=2)

root.mainloop()
