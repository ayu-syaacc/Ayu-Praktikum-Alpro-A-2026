class MataKuliah:
 def __init__(self, NamaMK, SKS, Dosen):
  self.NamaMK = NamaMK
  self.SKS = SKS
  self.Dosen = Dosen

def tampilkanMK(self):
  print("Nama Mata Kuliah:", self.NamaMK)
  print("SKS:", self.SKS)
  print("Dosen:", self.Dosen)

def ubahDosen(self, DosenLagi):
 self.Dosen = DosenLagi

MK1 = MataKuliah("Kalkulus", 3, "buk ririn")
MK2 = MataKuliah("Statistika", 3, "buk Aisha")
MK3 = MataKuliah("Alpro", 3, "buk reny")

print(MK1.NamaMK)
MK1.NamaMK = "Aljabar"
print(MK1.NamaMK)

print(ubahDosen(MK1, "buk Novery"))
print(MK1.Dosen)
