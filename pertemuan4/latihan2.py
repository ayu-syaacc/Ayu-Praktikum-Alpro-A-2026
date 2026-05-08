try:
    angka = int(input('Masukkan angka: '))
    angka_pemb = int(input('Masukkan angka pembagi: '))

    hasil = angka/angka_pemb
    print(f'Hasil: {hasil}')
except ZeroDivisionError:
    print('Error: Pembagi nda boleh nol yah')
except ValueError:
    print('Error: Harus memasukkan angka yah')
finally:
    print('udah yah')