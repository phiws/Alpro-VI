# no_akun = int(input("Masukan no akun :"))
# nama = input("Masukan nama :")
# saldo = float(input("Masukan saldo :"))
# is_premium = bool(input("Premium :"))
# list =  [no_akun,  nama, saldo, is_premium]

# if is_premium:
#     print("benar")
# else:
#     print("Anda tidak premium")
# combine = no_akun + nama + saldo + is_premium
# print("Hasil :",(no_akun, nama, saldo, is_premium))
# print (list)

#No 2
for i in range(10, 0, -1):
    hasil = 5 * i
    print(f"5 * {i} = {hasil}")

def Calculate_heart_healt(usia, detak_jantung, aktivitas):
    presentase_djm = (detak_jantung / 220 - usia ) *100
    return presentase_djm

hasil = Calculate_heart_healt()
usia = 30
detak_jantung = 150
aktivitas = "sedentari"
hasil = Calculate_heart_health (usia, detak_jantung, aktivitas)
perbandingan = hasil < hasil
print(perbandingan)