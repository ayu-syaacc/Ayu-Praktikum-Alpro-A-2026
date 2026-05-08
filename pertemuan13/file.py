import time
#tida ada output
f = open("contoh.txt", "rt")

# rt = read text
print(f.read())

f.close()

with open("contoh.txt") as f:
    print(f.read(5))

    print(f.readline())

    for x in f:
        print(x)

with open("contoh.txt", "a") as f:
    f.write("\nNim: 25071207453")

time.sleep(5)

with open("contoh.txt", "w") as f:
    f.write("Ke Overwrite")

with open("file_baru.txt", "x") as f: #
    pass

import os
if os.path.exists("file_baru.txt"):
    os.remove("file_baru.txt")
else:
    print("file tidak ada")

