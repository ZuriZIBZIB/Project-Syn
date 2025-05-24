print("\n===Kalkulator Sederhana===\n")

angka1 = int(input("Angka 1 : "))
operator = (input("Pilih  Operasi : "))
angka2 = int(input("Angka 2 : "))

if operator == "+" :
    hasil = (angka1 + angka2)
    print("Hasilnya adalahh : ",hasil)

elif operator == "-" :
    hasil = (angka1 - angka2)
    print("Hasilnya adalahh : ",hasil)

elif operator == "*" or operator == "x" :
    hasil = (angka1 * angka2)
    print("Hasilnya adalahh : ",hasil)

elif operator == "/" :
    hasil = (angka1 / angka2)
    print("Hasilnya adalahh : ",hasil)

else :
    print("Pastikan Anda Input Dengan Benar")

print("\nThis Is End Of Program\n")