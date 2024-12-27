# List Tuple & set, Dectionary

# List / Array []
#! Tipe deta : int, str, float, bool


# angka_1 = 1
# nama = "Agi"
# ip = 0.4
# is_mahasiswa = true

# list_angka = [1, "Agi", 0.4, True]
# print(list_angka[0]) # 1
# print(list_angka[1]) # Agi
# print(list_angka[2]) # 0.4
# print(list_angka[3]) # True
# print(list_angka[5]) # Error Index out of range 
# print(list_angka[-1]) Dari belakang 

# index_angka = list_angka[1]



# tambahan nilai  gagal

# list_genap = [ 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]  # index baris dari 1 bukan 0

# index_3 = list_genap[2]
# index_4 = list_genap[-4]

# pj = index_3 + index_4 

# print(f"panjang list : {len(list_genap)}")
# print(f"index ke 3 : {index_3}")
# print(f"index ke 4 : {index_4}")
# print (f"penjumlahan index ke 3 dan 4 : {pj}")




list_genap = [ 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# index ke 0 = 2
# index ke 1 = 4
# index ke 2 = 6
# ......
# index ke 9 = 20

# # cara 1 -> value
# for value in list_genap:
#     print (f"index ke : {value}")

# cara 2 -> index
# for index in range(len(list_genap)):
#     print (index) # index ke 0, 1, 2, 3, 4, 5
#     print (f"index ke {index}: {list_genap[index]}")

# cara 3 -> index dan value
for index, value in enumerate(list_genap): # (0, 2) # enumerate = mengembalikan index dan value
    print (f"index ke {index}: {value}")