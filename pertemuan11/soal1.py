def linearsearch(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

pasien = [
    "Budi Santoso", "Siti Rahayu", "Ahmad Fauzi", "Dewi Lestari",
    "Eko Prasetyo", "Fitri Handayani", "Gilang Ramadan", "Hana Pertiwi",
    "Irfan Maulana", "Joko Susilo"
]

target = input("Masukkan nama pasien yang dicari: ")
result = linearsearch(pasien, target)

if result != -1:
  print(f"{target} ditemukan di urutan ke-{result + 1}.")
else:
  print(f"{target} tidak ada dalam daftar hari ini.")

