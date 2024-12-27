BB = float(input("Inputkan berat_badan: "))
TB = float(input("Inputkan tinggi_badan: "))
bmi = BB / (TB ** 2)

if bmi < 18.5:
    print("Underweight")
elif bmi < 24.5 and bmi >=18.5:
    print("Normal")
elif bmi < 29.9 and bmi >=25:
    print("Overweight")
elif bmi > 30:
    print("Obesity")
else :
    print()