menu =  [["mi Goreng", 15000], 
         ["Es jeruk", 5000], 
         ["ayam geprek", 18000], 
         ["seblak", 13000], 
         ["mi rebus", 10000]]

def ini_menu():
    for x in menu:
        print(menu)

ini_menu()

a = int(input("masukkan nomor menu: "))

while True:
    a = input("masukkan nama pesanan: ")
    b = int(input("jumlah pesanan: "))

    pesanan =[[a, b],]

    