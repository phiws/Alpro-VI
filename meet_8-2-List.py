# List
#! List Manipulation

# Cara mengubah value
list_nama = ["Jett", "reyna", "chamber"]
print(f" Sebelum diubah : {list_nama}")
list_nama [1] = "Omen"
print(f" Setelah diubah : {list_nama}")
print ("=" * 95)

# Menambahkan / mengingput Value Baru
#! Apeend -> Inputkan Value baru di paling belakang
print(f" Sebelum Append : {list_nama}")
list_nama.append("Iso")
print(f" Setelah Append : {list_nama}")
print ("=" * 95)

#! Insert -> Inputkan Value baru sesuai 
print(f" Sebelum Insert : {list_nama}")
list_nama.insert(1, "raze")
print(f" Setelah Append : {list_nama}")
print ("=" * 95)

# Menghapus Value
#! Pop -> Menghapus Value yang paling terahir
print(f" Sebelum Pop : {list_nama}")
list_nama.pop()
print(f" Setelah Pop : {list_nama}")
print ("=" * 95)

# Remove -> Menghapus Value yang lebih spesifik
print(f" Sebelum Remove : {list_nama}")
list_nama.remove("Jett")
print(f" Setelah Remove : {list_nama}")
print ("=" * 95)

# Mengurutkan Value
list_angka = [0,1,2,3,4,5,6,7,8,14,1515,64,74,66,865]
# Ascending / Sort -> Mengurutkan Value dari kecil ke besar
print(f" Sebelum Sort : {list_nama}")
list_nama.sort()
print(f" Setelah Soret : {list_nama}")
print ("=" * 95)

# Descending / Reverse -> Mengurutkan Value dari besar ke kecil
print(f" Sebelum Reverse : {list_nama}")
list_nama.reverse()
print(f" Setelah Reverse : {list_nama}")
print ("=" * 95)

# Count -> Menghitung jumlah Value
print (f"Jumlah angka 3 :{list_angka.count(3)}")

#! Penggabungan 
list_nama_tambahan = ["Valorant", "Minecraft"]

# Extend -> Menggabungkan List dengan List lainnya
print(f" Sebelum Extend : {list_nama}") 
list_nama.extend(list_nama_tambahan)
print(f" Setelah Extend : {list_nama}")
print ("=" * 95)

# Operator "+"
list_delete = ["Daniel", "Lee jihon"]
for value in list_delete:
    list_nama.remove (value)
print(f"Setelah remove : {list_nama}")
