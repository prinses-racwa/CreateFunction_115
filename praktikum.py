#soal1
def convert_temperature (value, unit):
    if (unit == 'c'):
        return (value * 9 / 5) + 32
    elif (unit == 'f'):
        return (value - 32) * 5 / 9
    else:
        return None

input_value = float(input("masukkan value: "))
input_unit = input("masukkan unit (c/f): ")

konversi = convert_temperature(input_value, input_unit)
if (input_unit == 'c'):
    print(f"{input_value} derajat Celsius = {konversi} derajat Fahrenheit")
elif (input_unit == 'f'):
    print(f"{input_value} derajat Fahrenheit = {konversi} derajat Celsius")

#soal2

r = float(input("masukkan jari-jari lingkaran: "))
luas_lingkaran = lambda r: 3.14 * r * r

luas = luas_lingkaran(r)
print("Luas lingkaran dengan jari-jari", r, "adalah", luas)