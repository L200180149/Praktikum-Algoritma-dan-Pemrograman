from tkinter import *

my_app = Tk(className='Aplikasi dengan Label berbagai properti widget')

L1 = Label(my_app, text="Data Diri", font=('Arial', 24))
L1.grid(row=0, column=0, sticky='w')
L2 = Label(my_app, text="Nama")
L2.grid(row=1, column=0, sticky='w')
L3 = Label(my_app, text="Nur Fauzi Saputro")
L3.grid(row=1, column=1, sticky='w')
L4 = Label(my_app, text="NIM")
L4.grid(row=2, column=0, sticky='w')
L5 = Label(my_app, text="L200180149")
L5.grid(row=2, column=1, sticky='w')
L6 = Label(my_app, text="Bulu Favorit")
L6.grid(row=3, column=0, sticky='w')
L7 = Label(my_app, text="Tentang Kita")
L7.grid(row=3, column=1, sticky='w')
L8 = Label(my_app, text="Idola di Kalangan Sahabat")
L8.grid(row=4, column=0, sticky='w')
L9 = Label(my_app, text="Ali bin Abi Thalib")
L9.grid(row=4, column=1, sticky='w')
L10 = Label(my_app, text="Motto")
L10.grid(row=5, column=0, sticky='w')
L11 = Label(my_app, text="Hidup seperti sepeda, harus bergerak agar seimbang")
L11.grid(row=5, column=1, sticky='w')

def tutup():
    my_app.destroy()
    
B1 = Button(my_app, text="Tutup", command=tutup)
B1.grid(row=6, column=1)

my_app.mainloop()
