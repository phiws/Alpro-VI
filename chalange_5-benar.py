# awal = int(input("nilai awal: "))
# nilai_ahir = 5240411209

# while awal <= nilai_ahir:
#     if awal % 5 == 0:
#         print (awal)
#     if awal % 7 == 0:
#         print({awal}, "Kelipatan 7")
#     if awal % 7 == 0 and awal % 5 == 0:
#         print("boom")
#     else :
#         print()
#     awal += 1

awal = int(input("nilai awal: "))
nilai_akhir = 209

while awal <= nilai_akhir:
    if awal % 5 == 0 and awal % 7 == 0:
        print("boom")
    elif awal % 5 == 0:
        print(awal)
    elif awal % 7 == 0:
        print(f"{awal} Kelipatan 7")
    else:
        print()
    
    if awal == nilai_akhir:
        print("boom")
        break
    
    awal += 1