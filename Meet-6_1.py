# Function :  kumpulan / set perintah
    # Function biasa
    # Function dengan parameter (input)
    # Function dengan return

    #! syntax :
    #! def nama_function() : -> nama _function (huruf kecil)
        #! perintah

#? Function biasa
# def perkenalan ():
#     npm = 135
#     nama = "widi"
#     asal = "bali"
#     print("Npm ku 135")
#     print("Nama ku widi")
#     print("Aku berasal dari bali")

# perkenalan()



# def menghitung_luas ():
#     panjang = 10
#     lebar = 5
#     luas  = panjang * lebar
#     print("Luas = ", luas)

# menghitung_luas()



#?  Function dengan parameter (input)
    #! def  nama_function (parameter1, parameter2):

# def perkenalan (npm, nama, asal):
#     print("Npmku :", npm)
#     print("Namaku :", nama)
#     print("Aku berasal dari :", asal)

# perkenalan( 135, "widi", "bali")



#duplikasi menghitung luas tapi pakai parameter
    #! panjang, luas

# def menghitung_luas (panjang, lebar):
#     l =  panjang * luas
#     print("panjangnya :", panjang)
#     print("luasnya :", lebar)
#     print("hasilnya :", l)

# menghitung_luas(panjang=10, luas=5)

# def menghitung_luas (panjang, lebar):
#     luas  = panjang * lebar
#     print("Luas = ", luas)

# menghitung_luas(panjang=10, lebar=5)


#untuk luas segitiga
# luas = 0.5 * alas * tinggi

# def menghitung_luas (alas, tinggi):
#     luas  = 0.5 * alas * tinggi
#     print("Luas = ", luas)

# menghitung_luas(alas= 20, tinggi= 10)

def menghitung_luas ():
    tinggi = int(input("inputkan tinggi :"))
    alas = int(input("inputkan alas :"))
    luas  = 0.5 * alas * tinggi
    print("Luas = ", luas)

# menghitung_luas()

#Function dengan return
# def hello ():
#     return "hello world"

# hello() 

# def luas_persegi_panjang(panjnag, lebar):
#     luas = panjnag * lebar
#     return luas

# print(luas_persegi_panjang(10, 15)) sama dengan ->

# luas_lama =  luas_persegi_panjang(10, 15)
# luas_baru = luas_lama * 2
# print (luas)


def input_panjang():
    panjang = int(input("Masukkan panjang : "))
    return panjang

def input_lebar():
    lebar = int(input("masukkan lebar :"))
    return lebar

def hitung_luas():
    panjang = int(input("Masukkan panjang : "))
    lebar = int(input("masukkan lebar :"))
    return panjang * lebar

luas = hitung_luas()
print ("Luasnya : ", luas)
