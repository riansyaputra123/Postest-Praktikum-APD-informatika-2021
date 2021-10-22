print("====="*10, "\nSelamat datang di portal registrasi!")
print("Silahkan isi data anda dengan benar!")

data1 = input("Nama lengkap: ")
data2 = int(input("Nim: "))
data3 = int(input("Usia: "))
data4 = float(input("Tinggi badan anda: "))
data5 = input("Asal universitas: ")
data6 = input("Bikin password: ")

bio = [data1, data2, data3, data4, data5, data6]

print("====="*10, "\nPembuatan akun selesai silahkan login kembali")

x = int(input("Masukkan Nim: "))
y = input("Masukkan Password: ")

while  not x == bio[1] or not y == bio[5]:
    print("Nim atau Pasword salah!")
    x = int(input("Masukkan Nim: "))
    y = input("Masukkan Password: ")
else:
   print("====="*10,"\nLogin Berhasil!")
   print("Selamat Datang", bio[0]+"!")

matkul = {"sc1": "Pendidikan pancasila", "sc2": "ISBD", "sc3": "PTI", "sc4": "Fisika dasar", "sc5": " Pendidikan agama Islam", "sc6": "Kalkulus", "sc7": "Logika Informatika", "sc8": "Bahasa inggris 1", "sc9": "APD"}

print("Apa yang ingin anda akses: ","\n1.Jadwal mata kuliah saya","\n2.Biodata saya","\n3.Logout")
a = int(input("Pilih 1/2/3?: "))

if a == 1:
    print("====="*10, "\nAnda ingin jadwal mata kuliah hari apa? :", "\n1.Senin", "\n2.Selasa", "\n3.Rabu", "\n4.Kamis", "\n5.Jum'at")
    b = int(input("Pilih 1/2/3/4/5: "))
    
    if b == 1:
        print("====="*10+"\nJadwal hari senin adalah", matkul.get("sc1"), "dan", matkul.get("sc2"), "\n"+"====="*10)
    elif b == 2:
        print("====="*10+"\nJadwal hari selasa adalah", matkul.get("sc3"), "dan", matkul.get("sc4"), "\n"+"====="*10)
    elif b == 3:
        print("====="*10+"\nJadwal hari rabu adalah", matkul.get("sc5"), "\n"+"====="*10)
    elif b == 4:
        print("====="*10+"\nJadwal hari kamis adalah", matkul.get("sc6"), "dan", matkul.get("sc7"), "\n"+"====="*10)
    elif b == 5:
        print("====="*10+"\nJadwal hari jum'at adalah", matkul.get("sc8"), "dan", matkul.get("sc9"), "\n"+"====="*10)
elif a == 2:
    print("====="*10, "\nNama:",bio[0], "\nNim:",bio[1], "\nUsia:",bio[2], "\nTinggi badan:",bio[3], "\nAsal universitas:",bio[4], "\n"+"====="*10)
elif a == 3:
    print("====="*10, "\nLogout Berhasil!", "\n"+"====="*10)