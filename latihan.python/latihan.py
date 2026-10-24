# belajar day1 variabel&tipe data
nama = input ("siapa nama kamu ")
# print ((nama) + "" + "!")

umur = int(input("umur kamu berapa "))
# print (str(umur + 1) )
print ("halo" +  nama  + ", umur kamu sekarang " + str(umur) + "!" )

# belajar day2 tuple
nilai_ujian = [80,75,90,95,85,70]
print("nilai tertinggi", max(nilai_ujian))
print("nilai terrendah",min(nilai_ujian))

# belajar day2 dictionary
mahasiswa = {
    "nama": "ahmad jaki",
    "umur": 20,
    "jurusan":"sistem informasi",
}
for key,valeu in mahasiswa.items():
    
    print (key, ".", valeu)

# belajar python day 2 (if else&elif)
nilai = int(input("masukan nilai kamu: "))

if nilai >= 80:
    print("nilai A")
elif nilai >=70:
    print("nilai b")
elif nilai >=60:
    print("nilai c")
else:
    print("kamu tidak lulus")

for i in range(11):
    print(i)
    
    
angka = 1    
while angka <= 10:
    print(angka)   
    angka = angka + 1 
print("selesai")

total = 0
jumlah_data = int(input("ada berapa produk? "))

for i in range(jumlah_data):
    nilai = int(input("Masukkan harga : "))
    total = total + nilai
rata_rata = total / jumlah_data
print("Total semua harga:", total)
print("rata rata harga:",rata_rata)