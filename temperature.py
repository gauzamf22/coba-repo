#Converttemperature

dash = "------------------------------------------"
print(dash)
print("Temperature Converter")
print(dash)
print("This program converts temperatures between Celsius and Fahrenheit to each other :)")
print(dash)

print("Please enter the temperature you want to convert:")
print(dash)

unit = input("Enter the temperature unit (C for Celsius and F for Fahrenheit : ")
temperature = float(input("Enter the temperature value: "))

if unit == 'C':
    converted_temp = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {converted_temp}°F")
elif unit == 'F':
    converted_temp = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {converted_temp}°C")

else:
    print("Invalid unit. Please enter C/F.")

print(dash)
print("Thank you for using the Temperature Converter!")
print(dash)

#logical operator = evaluate multiple conditions (or, and, and not)
#or = intinya jika salah satu kondisi benar, maka hasilnya benar
#and = artinya jika 2 atau lebih kondisi benar, maka hasilnya benar
#not = intinya Fungsi not pada Python adalah operator logika yang digunakan untuk membalikkan nilai kebenaran dari suatu ekspresi. Jika ekspresi awalnya bernilai True, maka not akan mengembalikannya menjadi False, dan sebaliknya. Operator not hanya membutuhkan satu operand

#COntoh

temp = 35
is_raining = False

if temp > 30 or temp < 0 or is_raining:
    print("It's a hot or cold a day or it's not raining.")
else:
    print("Aman euy, lets ngopi!!!")

temp = 25
is_sunny = True

if temp > 20 and is_sunny:
    print("Sunny ges")
elif temp <=10 and not is_sunny:
    #berarti is sunny = False
    print("Uadem bos")
