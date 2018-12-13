from tkinter import *
my_app = Tk(className='Simple Calculate')

L1 = Label(my_app, text="Angka 1")
L1.grid(row=0, column=0)
int1 = IntVar()
E1 = Entry(my_app, textvariable=int1)
E1.grid(row=0, column=1, columnspan=3)
L2 = Label(my_app, text="Angka 2")
L2.grid(row=1, column=0)
int2 = IntVar()
E2 = Entry(my_app, textvariable=int2)
E2.grid(row=1, column=1, columnspan=3)

def tambah():
    a = int1.get() + int2.get()
    L3.config(text=a)
    
def kurang():
    b = int1.get() - int2.get()
    L3.config(text=b)
    
def kali():
    c = int1.get() * int2.get()
    L3.config(text=c)
    
def bagi():
    d = int1.get() / int2.get()
    L3.config(text=d)


B1 = Button(my_app, text=" + ", font=('Arial', 16), command=tambah)
B1.grid(row=2, column=0)
B1 = Button(my_app, text=" - ", font=('Arial', 16), command=kurang)
B1.grid(row=2, column=1)
B1 = Button(my_app, text=" X ", font=('Arial', 16), command=kali)
B1.grid(row=2, column=2)
B1 = Button(my_app, text=" : ", font=('Arial', 16), command=bagi)
B1.grid(row=2, column=3)

L4 = Label(my_app, text="Hasil")
L4.grid(row=3, column = 0)
L3 = Label(my_app, text="0")
L3.grid(row=3, column=3)

my_app.mainloop()
