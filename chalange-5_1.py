awal = int(input("nilai awal: "))
nilai_ahir = 209

while awal <= nilai_ahir:
    if awal % 5 == 0:
        print("Kelipatan 5", awal)
    if awal % 7 == 0:
        print("Kelipatan 7", awal)
    if awal % 7 == 0 and awal % 5 == 0:
        print("boom")
    awal += 1