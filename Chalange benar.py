def header():
    print(f"{'Program Menghitung Luas Bentuk Geometri' :^50}")
    print(f"{'Persegi Panjang' :^50}")
    print(f"{'Segitiga' :^50}")
    print("=" * 50)
header()

def Hitung_panjang():
    panjang = int(input("Masukkan panjang : "))
    lebar = int(input("Masukkan lebar : "))   
    return panjang * lebar

def Hitung_segitiga():
    panjang = int(input("Masukkan panjang : "))
    tinggi = int(input("Masukkan lebar : "))
    return panjang * tinggi / 2

while True:
    print ("Pilih salah satu ")
    print("Ketik  1 untuk persegi panjang")
    print("Ketik 2 untuk segitiga")
    pilihan = int(input("Masukkan pilihan :"))

    if pilihan == 1 :
        hasil = Hitung_panjang()
        print("Hasilnya :", hasil)

    elif pilihan == 2 :
        hasil = Hitung_segitiga()
        print("Hasilnya :", hasil)
        break
    else:
        print("Terjadi kesalahan")