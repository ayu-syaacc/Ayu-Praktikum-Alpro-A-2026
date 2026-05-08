x = input("Masukkan kode buku yang dicari: ")
def linearsearch(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

rak_a = ["BK-045", "BK-012", "BK-078", "BK-033", "BK-091","BK-027", "BK-056"]
result = linearsearch(rak_a, x)

print("🔍 Mencari di Rak A (Linear Search)...")
if result != -1:
    
    print(f"{x} ditemukan di rak A, posisi ke-{result}.")
else:
    print(f"{x} tidak ditemukan di rak A.")


def binarySearch(data, targetVal):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        y += 1

        if data[mid] == targetVal:
            return mid

        if data[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1
    return -1
    
rak_b = ["BK-011", "BK-023", "BK-035", "BK-047", "BK-059","BK-071", "BK-083", "BK-095"]
result = binarySearch(rak_b, x)

print("🔍 Mencari di Rak B (Binary Search)...")
if result != -1:
    print(f"{x} ditemukan di rak B, posisi ke-{result}.")
else:

    print(f"{x} tidak ditemukan di rak B.")

print("Kesimpulan: " + (f"{x} tersedia di Rak B." if result != -1 else f"{x} tidak tersedia di Rak B."))