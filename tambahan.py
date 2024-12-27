for i in range (50, 12, -1):
    print(i)
    if i % 3 == 0:
        print("Kelipatan 3")
    print(i)
    if i % 5 == 0:
        print("Kelipatan 5")
else:
    print(i)


def luas_trapeseium(a,b,t):
    luas = ((a+b)*t)/2
    return luas

a = float(input(f"masukkan nilai a:"))
b = float(input(f"masukkan nilai b:"))
c = float(input(f"masukkan nilai c:"))

luas =  luas_trapeseium(a,b,c)
print(f"luas trapeseium adalah {luas}")