#soal 1
n = 21
def fizzbuzz_plus(n):
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
         print("FizzBuzz")
        elif i % 3 == 0:
         print("Fizz")
        elif i % 5 == 0:
         print("Buzz")
        elif i % 7 == 0:
         print("Seven")
        else:
          print(i)

#soal 3
def hitung_nilai(tugas, uts, uas):
 nilaiAkhir = (30/100 * tugas) + (30/100 * uts) + (40/100 * uas)
 if nilaiAkhir >= 85:
  print("A")
 elif nilaiAkhir >= 70:
  print("B")
 elif nilaiAkhir >= 55:
  print("C")
 elif nilaiAkhir >= 40:
  print("D")
 else:
  print("E")
