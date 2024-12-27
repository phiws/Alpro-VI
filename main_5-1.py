# Perulangan 
# While

# while True: #1 true benar

aw = 0
ah = 10
while aw < ah:
    print ("209")
    aw += 1 #nilai awal = awal + 2 -> 0, 2, 4, ....
print ("perulangan berakhir")


# While dengan if
# Print nilai 1 - 10
#! Ketika bilangan genap print aku bilang genap
# else: print nilai

aw = 1
ah = 10
while aw <= ah:
    if aw % 3 == 0:
        print("Kelipatan 3")
    else:
        print (aw)
    aw += 1  


# Break, Continue, 
# Break berhenti perulangan
aw = 1
ah = 10
while aw <= ah:
    print ("hello word", aw)
    if aw == 8:
        break 
    aw += 1

# Continue 
aw = 1
ah = 10
while aw <= ah:
    print ("hello word", aw)
    if aw == 5:
        print ("Aku disini")  
        aw += 1    
        continue # mengabaikan baris selanjutnya
    print("Lanjut")
    aw += 1  


# For loop -> hello world 5x
for i in range(5):
    print ("hello world", i) 

# buat segitiga siku" tinggi 5 -> 1
for i in range(5, 0,-1):
    print('*' * i)


# Tipe data list, tiple, dictionary
nama = "widi"
genap = [2,4,6,8,10]
for i in genap:
    print(i)