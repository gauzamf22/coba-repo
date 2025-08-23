# Conditional Expressions (Ternary Operator)
# Ternary operator adalah cara singkat untuk menulis if-else dalam satu baris
# kayak shortcut gitu buat kondisi if - elsa

num = int(input("Masukkan angka: "))

print("Positive" if num > 0 else "Negative or Zero")
result = "Even" if num % 2 == 0 else "Odd"
# maksudaya adalah, sisa pembagiannya habis semua apabila dibagi dengan bilangan genap, alias 0
# even genasp, odd ganjil
# jadi kalau misalnya num % 2 == 0, maka resultnya adalah Even,

print(f"The number {num} is {result}.")

# modulus itu digunakan untuk mencari sisa hasil pembagian antara 2 bilangan 
# MSALNYA 10 % 3,sisanya pasti 1, 10 

num1 = int(input("Masukkan angka pertama: "))
num2 = int(input("Masukkan angka kedua: "))

max_num = num1 if num1 > num2 else num2
min_num = num1 if num1 < num2 else num2
print(f"Angka terbesar adalah {max_num} dan angka terkecil adalah {min_num}")

age = int(input("Masukkan umur Anda: "))

result = "Dewasa" if age >= 17 else "Anak-anak"
print(f"Anda adalah {result}.")
