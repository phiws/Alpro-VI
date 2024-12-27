# Operator Logika
# and -> kedua nilai benar
nilai_1 = True 
nilai_2 = False
nilai_3 = False
hasil = nilai_1 and nilai_2 and nilai_3
logika = print(f"{nilai_1} and {nilai_2} = {nilai_3}")

# or -> salah satu benar
nilai_1 = True
nilai_2 = False
hasil = nilai_1 or nilai_2
print(f"{nilai_1} or {nilai_2} = {hasil}")

# not -> negasi/nilai lawan
a = True
hasil = not a
print(f"Not ({a}) adalah {hasil}")

# xor -> "^" -> tidak ada nilai yang sama
nilai_1 = False
nilai_2 = False
hasil = (nilai_1 ^ nilai_2)
logika = print(f"{nilai_1} ^ {nilai_2} = {hasil}")