# Membuat Konversi Nilai sederhana
#! A : nilai >= 81
#! B : nilai >= 61
#! C : nilai >= 41
#! D : nilai >= 21
#! E : nilai < 21


#? minta inputan nilai
#! A : nilai >= 81 -> print = A
#! B : nilai >= 61
#! C : nilai >= 41
#! D : nilai >= 21
#! E : nilai < 21

ni = int(input("nilai :")) #JIKA INPUT NILAI HARUS ADA INT
if ni >= 81 :
    print("A")
elif ni >=61 :
    print("B")
elif ni >=41 :
    print("C")
elif ni >=21 :
    print("D")
else :
    print("E")