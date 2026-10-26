print("=== PROGRAM HITUNG DERET ARITMATIKA ===")

awal = int(input("Masukan Suku Pertama (a): "))
beda = int(input("Masukan Beda Deret (b) ")) 

banyak = int(input("Masukan Banyak Suku (n): "))
while banyak <= 0:
    print("Peringatan: Banyak suku harus lebih dari 0!")
    banyak = int(input("Silakan masukkan ulang Banyak Suku (n): "))

suku = awal 
total = 0

print("Barisan Deret: ", end="")
for i in range(banyak):
    print(suku, end=" ")
    total += suku
    suku += beda

print(f"Total Jumlah Seluru Deret= {total}")