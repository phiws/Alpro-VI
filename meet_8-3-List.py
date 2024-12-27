# Slicing -> memotong -> ":" -> [awal : akhir]
list_genap = [ 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
list_setelah_10 = list_genap[5:] # [10, 12, 14, 16, 18, 20]
list_sebelum_10 = list_genap[:3] # [2, 4, 6]

list_antara = list_genap[2:8] # [6, 8, 10, 12, 14, 16, 18]
# Or
list_antara = list_genap[2:-2] # [6, 8, 10, 12, 14, 16, 18]

# Print (list_genap)
# Print (list_setelah_10)
# Print (list_sebelum_10)
# Print (list_antara)

# Output : Value -> awal = 4, ahir = 7
for value in list_genap [:] :
    print ("Output :", value)