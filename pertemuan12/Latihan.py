struktur = { 
    "Skripsi_Aqil": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
            },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
            }
        },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                }
            }
        },
        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
        },
        "README.txt": 8
    }
}

#Tugas A — Hitung Total Ukuran
def total_ukuran(folder: dict) -> int:
    total = 0
    for item in folder.values():
        if isinstance(item, dict):
            total += total_ukuran(item)
        else:
            total += item
    return total

total_ukuran_skripsi = total_ukuran(struktur["Skripsi_Aqil"])
print(f"Total ukuran skripsi: {total_ukuran_skripsi} KB")

# Tugas B — Hitung Jumlah File
def hitung_file(folder: dict) -> int:
    count = 0
    for item in folder.values():
        if isinstance(item, dict):
            count += hitung_file(item)
        else:
            count += 1
    return count

jumlah_file_skripsi = hitung_file(struktur["Skripsi_Aqil"])
print(f"Jumlah file: {jumlah_file_skripsi} file")

# Tugas C — Cari File Terbesar
def cari_terbesar(folder: dict) -> tuple:
    terbesar = (None, 0)
    for item, ukuran in folder.items():
        if isinstance(ukuran, dict):
            sub_terbesar = cari_terbesar(ukuran)
            if sub_terbesar[1] > terbesar[1]:
                terbesar = sub_terbesar
        else:
            if ukuran > terbesar[1]:
                terbesar = (item, ukuran)
    return terbesar
file_terbesar = cari_terbesar(struktur["Skripsi_Aqil"])
print(f"File terbesar: {file_terbesar[0]} ({file_terbesar[1]} KB)")

# Tugas D — Cetak Struktur Folder
def tampilkan_tree(folder: dict, nama: str = "root", level: int = 0):
    indent = "    " * level
    print(f"{indent}📁 {nama}")
    for item, ukuran in folder.items():
        if isinstance(ukuran, dict):
            tampilkan_tree(ukuran, item, level + 1)
        else:
            print(f"{indent}    📄 {item} ({ukuran} KB)")
tampilkan_tree(struktur["Skripsi_Aqil"], "Skripsi_Aqil")
