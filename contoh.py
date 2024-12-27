# No 1
npm = float(input("Masukkan npm: "))
hasil = (npm * (1 + 10 / 31) ** 5) ** 2
print ("hasilnya :", hasil)
#No 2
for i in range(1, 11):
    hasil = 7 * i
    print(f"7 * {i} = {hasil}")
# No 3
def konversi_suhu(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

celcius = 30
fahrenheit = konversi_suhu(celcius)
hasil_perkalian = 7 * 10

print(f"{celcius} °C = {fahrenheit} °F")

if fahrenheit >= hasil_perkalian:
    print(f"Hasil konversi {fahrenheit} °F lebih besar {hasil_perkalian}.")
elif fahrenheit == hasil_perkalian:
    print(f"Hasil konversi {fahrenheit} °F sama dengan {hasil_perkalian}.")
else:
    print(f"Hasil konversi {fahrenheit} °F lebih kecil dari {hasil_perkalian}.")
# No 4s
bilangan = int(input("Masukkan bilangan bulat positif: "))

if bilangan > 0:  
    if bilangan % 2 == 0 and bilangan % 3 == 0: 
        print(f"Bilangan setelah ditambahkan 6: {bilangan}")
    elif bilangan % 2 != 0 and bilangan % 5 == 0: 
        bilangan += 12
        print(f"Hasil = {bilangan}")
    else:
        print("Tidak ada transformasi yang diterapkan.")
else:
    print()