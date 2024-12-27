#Kalkulus sederhana (2 inputan)
#Operator Aritmatika (+ - * / % // **)

print("="*32)
print("="*5, "kalkulator sederhana","-"*5)
print("="*32)

nilai1 = float(input("inputkan angka pertama :"))
nilai2 = float(input("inputkan angka kedua :"))
operator = input("inputkan operator :")
print("="*32)
if operator == "+":
    hasil = nilai1 + nilai2
    print(f"hasil {nilai1} + {nilai2} = {hasil}")
elif operator == "-":
    hasil = nilai1 - nilai2
    print(f"hasil {nilai1} - {nilai2} = {hasil}")
elif operator == "*":
    hasil = nilai1 * nilai2
    print(f"hasil {nilai1} * {nilai2} = {hasil}")
elif operator == "/":
    hasil = nilai1 / nilai2
    print(f"hasil {nilai1} / {nilai2} = {hasil}")
elif operator == "%":
    hasil = nilai1 % nilai2
    print(f"hasil {nilai1} % {nilai2} = {hasil}")
elif operator == "//":
    hasil = nilai1 - nilai2
    print(f"hasil {nilai1} // {nilai2} = {hasil}")
elif operator == "**":
    hasil = nilai1 ** nilai2
    print(f"hasil {nilai1} ** {nilai2} = {hasil}")
else :
    print("Eror")
print("="*32)