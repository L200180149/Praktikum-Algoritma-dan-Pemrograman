data = {'nim' : 'L200180149', 'nama' : 'Nur Fauzi Saputro',
        'alamat' : 'Klaten', 'umur' : '19 tahun', 'status' : 'Singlelillah',
        'kodepos' : '57424', 'prodi' : 'Informatika'}
def a():
    'Menampilkan NIM'
    print('NIM adalah ', data['nim'])
        
def v():
    'Menampilkan nama'
    print('Namanya adalah ', data['nama'])

def c():
    'Menampilkan umur'
    print('Umurnya adalah ', data['umur'])

def d():
    'Menampilkan alamat'
    print('Alamatnya di ', data['alamat'])

def e():
    'Menampilkan status'
    print('Statusnya dia masih ', data['status'])

def f():
    'Menampilkan kodepos'
    print('Kodeposnya ', data['kodepos'])

def g():
    'Menampilkan prodi'
    print('Dia di Prodi ', data['prodi'])

x = 's'
while x != 'k':
    print('Berikut akan ditampilkan data-data mengenai informasi pribadi, silahkan pilih untuk menampilkan informasi yang anda inginkan.')

    print('Pencet b untuk membuka bantuan')

    x = str(input('PILIHH BUJANKKK: '))

    if x == 'b' :
            print("Pilihan yang tersedia :")
            print('a menampilkan NIM')
            print('v menampilkan Nama Saya')
            print('c menampilkan Umur Saya')
            print('d menampilkan Alamat Saya')
            print('e menampilkan Status Saya')
            print('f menampilkan Kodepos Saya')
            print('g menampilkan Prodi Saya')

    elif x == 'a' :
            a()
    elif x == 'v' :
            v()
    elif x == 'c' :
            c()
    elif x == 'd' :
            d()
    elif x == 'e' :
            e()
    elif x == 'e' :
            e()
    elif x == 'f' :
            f()
    elif x == 'g' :
            g()

print("Terima Kasih")
