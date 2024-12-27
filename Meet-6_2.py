#Program sederhana untuk menghitung keliling persegi panjang

# header 
def header():
    print(f"{'PROGRAM MENGHITUNG LUAS & KELILING' :^50}")
    print(f"{'PERSEGI PANJANG' :^50}")
    print("=" * 50)

header()

# Inputkan user
def inputkan_user():
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    return panjang, lebar


# Menghitung luas
def hitung_luas(panjang, lebar):
    luas  = panjang * lebar
    return  luas

# Menghitung keliling 
def hitung_keliling(panjang, lebar):
    keliling = 2 * (panjang + lebar)
    return keliling

# Menampilkan Output
def menampilkan_output(panjang, lebar, luas, keliling ):
    print(f"Panjang\t\t: {panjang}")
    print(f"lebar\t\t: {lebar}")
    print(f"luas\t\t: {luas}")
    print(f"keliling\t\t: {keliling}")

# Looping
header()
while True:
    panjang, lebar = inputkan_user()
    luas = hitung_luas(panjang=panjang, lebar=lebar)
    keliling = hitung_keliling(panjang=panjang, lebar=lebar)
    menampilkan_output(panjang, lebar,  luas, keliling)
    is_selesai = input("Apalah ingin lanjut (Y/N): ")
    if is_selesai.lower() == "n" or is_selesai == "N":
        break

    