from tkinter import *

my_app = Tk(className='Bangun Geometri Prisma')

L1 = Label(my_app, text='Bangun Geometri Prisma', font=('TNR', 20, 'bold'))
L1.grid(row=0, sticky='w')
L2 = Label(my_app, text='Dalam geometri, prisma adalah bangun ruang tiga dimensi yang dibatasi oleh alas dan tutup identik berbentuk segi-n dan sisi-sisi tegak.')
L2.grid(row=1, column=0, sticky='w')
L3 = Label(my_app, text='Dimensi pada Geometri dibedakan menjadi 2, yaitu Dimensi dua dan Dimensi tiga')
L3.grid(row=2, column=0, sticky='w')
L4 = Label(my_app, text='Contoh benda Geometri adalah permukaan kertas, bola, dll')
L4.grid(row=3, column=0, sticky='w')
L5 = Label(my_app, text='Bangun Geometri Prisma', font=('Calibri', 12, 'bold'))
L5.grid(row=4, column=0, sticky='w')
L6 = Label(my_app, text='Tinggi Alas :')
L6.grid(row=5, column=0, sticky='w')
e1 = Entry(my_app)
e1.grid(row=5, column=1, sticky='w')
L7 = Label(my_app, text='Lebar Alas :')
L7.grid(row=6, column=0, sticky='w')
e2 = Entry(my_app)
e2.grid(row=6, column=1, sticky='w')
L8 = Label(my_app, text='Tinggi Prisma')
L8.grid(row=7, column=0, sticky='w')
e3 = Entry(my_app)
e3.grid(row=7, column=1, sticky='w')

def luasalas():
    a = int(e1.get())
    b = int(e2.get())
    hasila = 0.5 * (a * b)
    return hasila

def kelalas():
    c = int(e2.get())
    h = int(e3.get())
    hasilkela = (3 * c) * h
    return hasilkela

def luasp() :
    luas = (2 * luasalas()) + (kelalas())
    L8.config(text=luas)

B1 = Button(my_app, text='Hitung Luas', command=luasp)
B1.grid(row=8, column=0, sticky='w')
L7 = Label(my_app, text='Luas =', font=('Calibri', 12, 'bold'))
L7.grid(row=8, column=1, sticky='w')
L8 = Label(my_app, text='0', font=('Calibri', 12, 'bold'))
L8.grid(row=8, column=2, sticky='w')

my_app.mainloop
