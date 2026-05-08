menu =  [["mi Goreng", 15000], ["Es jeruk", 5000], ["ayam geprek", 18000], ["seblak", 13000], ["mi rebus", 10000]]

for i in (menu):
    int(input("masukkan nomor menu: "))
    if i not in menu:
        print("[ERROR] pilihan tidak valid")
    else:
        print(i)