BB = float(input("Inputkan berat_badan: "))
TB = float(input("Inputkan tinggi_badan: "))

bmi = BB / (TB ** 2)
print("Hasil BMI:", bmi)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.5:
    print("Normal")
elif 24.5 <= bmi < 29.9:
    print("Overweight")
elif bmi >= 30:
    print("Obesity")
else :
    print()
