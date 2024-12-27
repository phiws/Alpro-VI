# Soal 1
# Metode Penilaian: Benar = 25; Salah = 20; Kosong = 0

npm = float(input("Inputkan 3 NPM terakhir: "))
hasil = npm * (1 + (10/31))**(5+2) # pastikan penggunaan tanda kurung yang tepat
print(f"Hasil yang benar: {hasil}")

# contoh yang salah
salah = npm * (1 + (10/31))**5+2
print(f"Hasil yang salah: {salah}")
# Hasil yang benar: 955.6280936395311
# Hasil yang salah: 548.3168340199818


# Soal 1
# Metode Penilaian: Benar = 25; Salah = 20; Kosong = 0

npm = float(input("Inputkan 3 NPM terakhir: "))
hasil = (npm * (1 + 35**(3-1)))/13 # pastikan penggunaan tanda kurung yang tepat
print(f"Hasil yang benar: {hasil}")

# contoh yang salah
salah = (npm * (1 + 35**3-1))/13
print(f"Hasil yang salah: {salah}")
# Hasil yang benar: 12731.538461538461
# Hasil yang salah: 445240.3846153846


# Soal 2
# Metode Penilaian: Benar = 35; Salah = 25; Kosong = 0

for i in range(1,11):
    print(f"7 x {i} = {7*i}")
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70


# Soal 2
# Metode Penilaian: Benar = 35; Salah = 25; Kosong = 0

for i in range(3,11):
    print(f"{i} + 13 / {i+1} = {i + 13 / (i+1)}")
# 3 + 13 / 4 = 6.25
# 4 + 13 / 5 = 6.6
# 5 + 13 / 6 = 7.166666666666666
# 6 + 13 / 7 = 7.857142857142858
# 7 + 13 / 8 = 8.625
# 8 + 13 / 9 = 9.444444444444445
# 9 + 13 / 10 = 10.3
# 10 + 13 / 11 = 11.181818181818182

# Soal 3
# Metode Penilaian: Benar = 30; Salah = 20; Kosong = 0

def konversi_suhu(celcius):
    fahrenheit = celcius * 9/5 + 32
    return fahrenheit

celcius = 30
hasil_konversi = konversi_suhu(30)

perbandingan = hasil_konversi >= hasil
print(perbandingan)

#False


# Soal 3
# Metode Penilaian: Benar = 30; Salah = 20; Kosong = 0

def luas_lingkaran(r):
    luas = (22/7) * (r**2)
    return luas

r = 49
hasil_luas = luas_lingkaran(30)

perbandingan = hasil_luas < hasil
print(perbandingan)
# True


# Soal 4
# Metode Penilaian: Benar = 10; Salah = 0; Kosong = 0

bilangan_bulat = int(input("Masukkan bilangan bulat: "))
print("Masukkan bilangan bulat: ", bilangan_bulat)

# Clue:
# Jika genap berarti habis dibagi 2
# Jika ganjil berarti tidak habis dibagi 2

if bilangan_bulat % 2 == 0 and bilangan_bulat % 3 == 0:
    bilangan_bulat += 6
    print(bilangan_bulat)
    # atau bisa juga dengan cara berikut
    # print(bilangan_bulat + 6)
elif bilangan_bulat % 2 != 0 and bilangan_bulat % 5 == 0:
    bilangan_bulat += 12
    print(bilangan_bulat)
    # atau bisa juga dengan cara berikut
    # print(bilangan_bulat - 3)
else:
    print("Tidak ada transformasi yang diterapkan")
# Masukkan bilangan bulat:  2
# Tidak ada transformasi yang diterapkan



# Soal 4
# Metode Penilaian: Benar = 10; Salah = 0; Kosong = 0

bilangan_bulat = int(input("Masukkan bilangan bulat: "))
print("Masukkan bilangan bulat: ", bilangan_bulat)

# Clue:
# Jika genap berarti habis dibagi 2
# Jika ganjil berarti tidak habis dibagi 2

if bilangan_bulat % 2 != 0 and bilangan_bulat % 3 == 0:
    bilangan_bulat /= 2
    print(bilangan_bulat)
    # atau bisa juga dengan cara berikut
    # print(bilangan_bulat / 2)
elif bilangan_bulat % 2 == 0 and bilangan_bulat % 5 == 0:
    bilangan_bulat *= 12
    print(bilangan_bulat)
    # atau bisa juga dengan cara berikut
    # print(bilangan_bulat * 3)
else:
    print("Tidak ada transformasi yang diterapkan")
# Masukkan bilangan bulat:  2
# Tidak ada transformasi yang diterapkan



# Soal 5
# Metode Penilaian: Benar = 10; Salah = -10; Kosong = 0

def find_lowest(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num1 and num2 < num3:
        return num2
    else:
        return num3

# Alternatif cara lain
def find_lowest_alternative(num1, num2, num3):
    return min(num1, num2, num3)

print(find_lowest(3, 2, 3))


# Soal 5
# Metode Penilaian: Benar = 10; Salah = -10; Kosong = 0

def find_highest(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

# Alternatif cara lain
def find_highest_alternative(num1, num2, num3):
    return max(num1, num2, num3)

print(find_highest(1, 2, 3))
