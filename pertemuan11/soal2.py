def binarySearch(data, targetVal):
    left = 0
    right = len(data) - 1
    y = 0
      
    while left <= right:
        y += 1
        mid = (left + right) // 2

        if data[mid] == targetVal:
            return mid

        if data[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1
    return -1
    

id_karyawan = [
    1021, 1045, 1089, 1102, 1157, 1203, 1245, 1312,
    1378, 1401, 1456, 1502, 1567, 1634, 1700
]
x = int(input("Masukkan ID karyawan yang dicari: "))

result = binarySearch(id_karyawan, x)

if result != -1:
  print(f"Proses perbandingan: {y} kali")
  print(f"ID {x} ditemukan! posisi ke-{result} dalam daftar.")
else:
  print(f"ID {x} tidak terdaftar sebagai karyawan.")
  print(f"Proses perbandingan: {y} kali")
