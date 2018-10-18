Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=== RESTART: C:\Users\TOSHIBA PC\Documents\Nur Fauzi Saputro L200180149.py ===
>>> ##Kegiatan 1
>>> ##Program Identitas Diri
>>> ##Dibuat oleh Nur Fauzi Saputro L200180149
>>> Nama
'Nur Fauzi Saputro'
>>> Alamat
'Alamat : Krapyak, Merbung, Klaten Selatan, Klaten.'
>>> Umur
'Umur : 18 tahun'
>>> Status
'Status : Lajang'
>>> Tempat_Lahir
'Tempat Lahir : Klaten'
>>> Tanggal_Lahir
'Tanggal Lahir : 25 Oktober 1999'
>>> NIM
'NIM : L200180149'
>>> Tahun_Masuk_UMS
'Tahun Masuk : 2018'
>>> Semester
'Semester : 1'
>>> Prodi
'Prodi : Informatika'
>>> 
>>> ##Kegiatan 2
>>> ##Program Akun
>>> ##Dibuat oleh Nur Fauzi Saputro L200180149
>>> Nama
'Nur Fauzi Saputro'
>>> Tanggal_Lahir
'Tanggal Lahir : 25 Oktober 1999'
>>> Nickname
'N.Fauzi.S'
>>> Username
'F199925'
>>> Password
'Nur9925'
>>> 
>>> ##Kegiatan 3
>>> ##Operator
>>> Nama = 'Nur Fauzi Saputro'
>>> NIM = 'L200180149'
>>> x = '1'+ NIM[7:]
>>> a = int(x)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> ##Respon yang diberikan python tersebut muncul karena perintah sebelumnya
>>> ##yaitu menanyakan tipe data apa yang tersimpan dalam variabel (a)
>>> ##dan tipe data yang tersimpan dalam variabel (a) adalah bilangan bulat
>>> ##dimana a merupakan konversi dari data string menjadi integer yang
>>> ##tersimpan didalam variabel (a)
>>> type(b)
<class 'int'>
>>> ##Respon tersebut muncul karena penyebab yang sama dengan type(a) yang ada
>>> ##di atas, hanya data yang tersimpan di dalam variabel (b) merupakan
>>> ##jumlah penghitungan karakter dari variabel (Nama) sehingga variabel
>>> ##(b) mempunyai tipe data integer atau bilangan bulat
>>> a / b
67.58823529411765
>>> ##Respon tersebut merupakan hasil dari operasi pembagian variabel (a)
>>> ##dengan variabel (b)
>>> a // b
67
>>> ##Respon tersebut merupakan hasil bulat pembagian variabel (a)
>>> ##dengan variabel (b) sehingga pembagian tanpa menghasilkan angka desimal
>>> 10 * (a-999)
1500
>>> ##Respon tersebut merupakan hasil pengoperasian perintah yang telah
>>> ##diberikan sebelumnya, yaitu seperti apa yang tertulis diatas
>>> 
>>> b ** 2
289
>>> ##Respon tersebut merupakan hasil darib dipangkat 2, sesuai dengan
>>> ##perintah yang tertulis diatas
>>> a % b
10
>>> ##Respon tersebut merupakan hasil sisa dari pembagian variabel
>>> ##(a) dengan variabel (b) sehingga menghasilkan bilangan 10
>>> 
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> ##Respon tersebut karena perintahnya merupakan menampilkan tipe data apa
>>> ##yang tersimpan di dalam variabel (c) dimana di variabel tersebut,
>>> ##data yang tersimpan adalah float, jadi respon yang muncul seperti
>>> ##yang telah tercantum diatas
>>> a / c
91.92
>>> ##Respon tersebut merupakan hasil dari operasi pembagian variabel
>>> ##(a) dengan variabel (c)
>>> a // c
91.0
>>> ##Respon tersebut merupakan hasil bulat pembagian variabel (a) dengan
>>> ##variabel (c). Mengapa harus ada .0 setelah angka 91? Karena data di
>>> ##di variabel (c) merupakan data float, sehingga hasil operasinya
>>> ##juga berupa data float
>>> a % c
11.5
>>> ##Respon tersebut merupakan hasil sisa dari pembagian variabel (a)
>>> ##dengan variabel (c) sehingga menghasilkan bilangan 11.5
>>> ##sekali lagi kenapa sisa pembagian bilangan berupa data float?
>>> ##karena data di variabel (c) merupakan data float, sehingga hasil
>>> ##dari operasi apapun hasilnya akan berupa float
>>> 
>>> c > b
False
>>> ##Respon tersebut merupakan hasil dari operasi logika, dimana menanyakan
>>> ##apakah c lebih besar dari b itu benar. dan jawabannya adalah salah
>>> ##tipe data yang berada pada respon berupa boolean
>>> type(c > b)
<class 'bool'>
>>> ##Respon tersebut merupakan tipe data apa yang tampil dari operasi
>>> ##c > b, dan jawabannya adalah tipe data tersebut berupa bool
>>> a > b and b > c
True
>>> ##Respon tersebut merupakan hasil dari operasi logika diatasnya
>>> ##dimana jika True and True maka hasil akhirnya juga berupa True
>>> a > 1100 or b < 10
True
>>> ##Respon tersebut juga merupakan hasil dari operasi logika diatasnya
>>> ##dimana perintah diatas menggunakan perintah 'or' bukan and lagi
>>> 
>>> 
>>> 
>>> ##Kegiatan 4
>>> ##Tipe Data
>>> ##Dibuat oleh Nur Fauzi Saputro L200180149
>>> 
>>> Nama = 'Nur Fauzi Saputro'
>>> NIM = 149
>>> Tinggi = 1.68
>>> Berat = 61
>>> Tahun_Lahir = 1999
>>> Aku = (Tahun_Lahir, Berat, Tinggi, NIM, Nama)
>>> Data = (Tahun_Lahir, Berat, Tinggi, NIM, Nama)
>>> 
>>> type(Aku)
<class 'tuple'>
>>> ##Respon tersebut menampilkan tipe data apa yang tersimpan di dalam
>>> ##variabel (Aku), dan data yang ada di dalamnya merupakan tipe data
>>> ##Tuple, sehingga muncullah seperti yang tercantum diatas
>>> Aku[0]
1999
>>> ##Respon tersebut menampilkan data di variabel (Aku) di indeks ke 0
>>> ##Dimana indeks ke 0 dari variabel (Aku) merupakan Tahun_Lahir
>>> ##sehingga yang tercantum adalah data Tahun_Lahir
>>> a = NIM % 4; Aku[a]
61
>>> ##Respon tersebut merupakan hasil indexing dari variabel (Aku)
>>> ##dengan indeks (a) dimana a merupakan hasil sisa pembagian NIM dibagi 4
>>> ##sehingga menghasilkan angka 1, dan data yang muncul merupakan indeks
>>> ##ke 1 dari variabel(Aku)
>>> type(Aku[a])
<class 'int'>
>>> ##Respon tersebut menampilkan tipe data apa yang terdapat pada indeks ke-a
>>> ##dari variabel (Aku). dan tipe data yang tersimpan pada indeks ke-a di
>>> ##variabel (Aku) berupa integer.
>>> Aku[a:4]
(61, 1.68, 149)
>>> ##Respon tersebut menampilkan Slicing dari variabel (Aku) dengan slicing
>>> ##dari indeks ke-a sampai 4, sehingga yang tercantum adalah data dari
>>> ##indeks ke-a hingga indeks ke-3
>>> type(Aku[4])
<class 'str'>
>>> ##Respon tersebut menampilkan tipe data apa yang tersimpan di dalam
>>> ##variabel (Aku) indeks ke 4, dimana indeks ke-4 dari variabel (Aku)
>>> ##berupa data string, jadi yang tercantum sebagai jawaban seperti tersebut
>>> Aku[0] = 'oke'
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    Aku[0] = 'oke'
TypeError: 'tuple' object does not support item assignment
>>> ##Respon python berupa error karena objek tidak mendukung perintah tersebut
>>> type(Data)
<class 'tuple'>
>>> ##Respon tersebut menampilkan tipe data apa yang tersimpan didalam variabel
>>> ##(Data), dan data yang ada didalamnya merupakan tipe data tuple, sehingga
>>> ##muncullah seperti apa yang tercantum diatas
>>> type(Data[4])
<class 'str'>
>>> ##Respon tersebut menampilkan tipe data apa yang tersimpan didalam variabel
>>> ##(Data) indeks ke-4 dimana indeks ke-4 dari variabel(Data) berupa data
>>> ##string, jadi yang tercantum sebagai jawaban tersebut
>>> Data[4][5]
'a'
>>> ##Respon tersebut menampilkan indexing dari variabel (Data) indeks ke-4
>>> ##indeks ke-5 sehingga yang muncul adalah apa yang seperti ada pada jawaban
>>> Data[4][a:6]
'ur Fa'
>>> ##Respon tersebut merupakan hasil slicing indeks ke-a sampai indeks ke-6
>>> ##dari indeks ke-4 variabel(Data)
>>> Data[0] = 'ok' ; Data
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    Data[0] = 'ok' ; Data
TypeError: 'tuple' object does not support item assignment
>>> ##Respon tersebut menghasilkan error karena perintah tidak sesuai dengan
>>> ##data yang ada
>>> Data[-a]
'Nur Fauzi Saputro'
>>> ##Respon merupakan hasil indexing ke-a dari belakang variabel (Data) dimana
>>> ##isinya berupa Nama, jadi yang ditampilkan pada hasil berupa nama
>>> range(a)
range(0, 1)
>>> ##Respon tersebut merupakan hasil range dengan batas bawah yaitu (a)
