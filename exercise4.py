import math

# untuk menghitung panjang sisi miring segitiga menggunakan rumus phytagoras

a = float(input("Masukkan panjang sisi a segitiga: "))
b = float(input("Masukkan panjang sisi b segitiga: "))


c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Panjang sisi miring segitiga dengan sisi a = {a} dan sisi b = {b} adalah: {c} cm")

