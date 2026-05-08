#Sistem Registrasi Peserta Event
class NamaError(Exception):
    pass

class UmurError(Exception):
    pass
 
print("=== REGISTRASI PESERTA SEMINAR ===")
try:
    while True:    
        try:
            nama = input("Nama Lengkap: ")
            if len(nama) < 3:
                raise NamaError
            break
        except NamaError:
            print('[ERROR] Nama terlalu pendek! Minimal 3 karakter.')

    while True: 
        try:
            umur = int(input("Umur: "))
            if umur < 17 or umur >60:
                raise UmurError
            break
        except UmurError:
            print('[ERROR] Umur tidak memenuhi syarat (17-60 tahun).')

    while True:
        try:
            email = input("Email: ")
            if "@" not in email:
                raise ValueError("[ERROR] Email tidak valid! Harus mengandung '@'.")
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            hp = input("No HP: ")
            if not hp.isdigit() or len(hp) < 10 or len(hp) > 13:
                raise ValueError("[ERROR] No HP tidak valid! Harus 10-13 digit angka.")
            break
        except ValueError as e:
            print(e)

finally:
    print("Proses input selesai.")

print()
print("=== DATA PESERTA ===")
print(f"Nama : {nama}")
print(f"Umur : {umur} tahun")
print(f"Email : {email}")
print(f"No HP : {hp}")
print("Status : TERDAFTAR")