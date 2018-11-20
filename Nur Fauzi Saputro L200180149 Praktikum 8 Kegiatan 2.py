def konversiSuhu(c = 0, f = 0):
    a = c * 1.8 + 32
    b = (f - 32) / 1.8
    if f == 0:
        print('Suhu', c, 'Celcius setara dengan', a, 'Fahrenheit')
    elif c == 0:
        print('Suhu', f, 'Fahrenheit setara dengan', b, 'Celcius')
