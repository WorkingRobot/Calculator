from tkinter import *
from functools import partial
import string

def showNum(num):
    if len(show.get()) < 19:
        show.set(show.get() + str(num))
def setOperator(opotype):
    if show.get().find("+") == -1 and show.get().find("-") == -1 and show.get().find("*") == -1 and show.get().find("/") == -1:
        global opo
        opo = opotype
        show.set(show.get()+opotype)
        return
    x = show.get()
    x = x.replace("+", opotype)
    x = x.replace("-", opotype)
    x = x.replace("*", opotype)
    x = x.replace("/", opotype)
    global opo
    opo = opotype
    show.set(x)
def calculate():
    show.set(eval(show.get()))

root = Tk()
root.title("Calculator")
root.iconbitmap(default="icon.ico")
show = StringVar()
opo = None

OutputEntry = Entry(state='readonly', textvariable=show, justify='right').grid(columnspan=4)

buttons = []
r = 1
c = 0
for buttonNum in range(1,10):
    func = partial(showNum, buttonNum)
    buttons.append(Button(root, text=buttonNum, command=func, padx=12))
    if c == 3:
        c = 0
        r += 1
    buttons[-1].grid(row=r, column=c)
    c += 1

opoButtons = []
r = 1
for opotype in ['+', '-', '*', '/']:
    func = partial(setOperator, opotype)
    opoButtons.append(Button(root, text=opotype, command=func))
    opoButtons[-1].grid(row=r, column=5)
    r += 1
opoButtons.append(Button(root, text="=", command=calculate))
opoButtons[-1].grid(row=4, column=2, columnspan=3)





mainloop()
