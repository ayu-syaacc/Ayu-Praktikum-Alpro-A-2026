#1
def C_tambah(A,B):
    baris, kolom = len(A), (len(A))
    hasil = [[A[i][j]+B[i][j] for j in range(kolom)] for i in 
range(baris)]
    return hasil
A = [[5, 3, 1],
     [2, 8, 4],
     [7, 8, 9]]
B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

C = C_tambah(A,B)
print("hasil penjumlahan: ")
for baris in C:
        print(baris)

#2
def C_kurang(A,B):
    baris, kolom = len(A), len(A)
    hasil = [[A[i][j] - B[i][j] for j in range(kolom)] for i in 
range(baris)] 
    return hasil 

D = C_kurang(A,B)
print("hasil pengurangan: ")
for baris in D:
     print(baris)

#3
def kali_skalar(A, k):
    hasil=[]
    for baris in A:
        baris_baru = [elemen * k for elemen in baris]
        hasil.append(baris_baru) 
    return hasil 
    
C_skalar= kali_skalar(A,4)
print("hasil skalar: ")
for baris in C_skalar:
    print(baris) 