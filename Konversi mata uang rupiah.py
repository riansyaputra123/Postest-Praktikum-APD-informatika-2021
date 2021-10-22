#Menu konversi rupiah
print("Silahkan pilih menu berikut: ")
print("1. Konversi ke USD (Dolar Amerika)\n2. Konversi ke SGD (Dolar Singapura)")
print("3. Konversi ke EUR (Euro)\n4. Konversi ke JPY (Yen Jepang)")

#inputan menu dan nominal rupiah dari user
menu = int(input("Silahkan pilih 1/2/3/4: "))
nilai = int(input("Masukkan nominal rupiah yang akan dikonversi: "))

#Proses konversi
nilai1 = nilai / 14119.95
nilai2 = nilai / 10505.45
nilai3 = nilai / 16435.41
nilai4 = nilai / 123.34

#Kondisi
if menu == 1 :
    print(nilai, "IDR setara dengan %.2f" %nilai1, "USD")
elif menu == 2 :
    print(nilai, "IDR setara dengan %.2f" %nilai2, "SGD")
elif menu == 3 :
    print(nilai, "IDR setara dengan %.2f" %nilai3, "EUR")
elif menu == 4 : 
    print(nilai, "IDR setara dengan %.2f" %nilai4, "JPY")

