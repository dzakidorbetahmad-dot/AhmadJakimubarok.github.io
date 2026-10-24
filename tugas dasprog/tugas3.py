nama = input("masukan nama:")
nis = int(input("masukan nis:"))
jurusan = input("masukan jurusan [si/sia]")

if jurusan == "si":
    nama_jurusan = 'sistem informasi'
    harga = 2400
elif jurusan == "sia":
    nama_jurusan = 'sistem informasi akutansi'
    harga = 2000
else :
    nama_jurusan = "nama jurusan tidak tersedia"
    harga = 0

print("=" * len("pendaftaran mahasiwa"))
print("pendaftaran mahasiwa")
print("=" * len("pendaftaran mahasiwa"))

print("nama :",nama)
print("nis :",nis)
print("jurusan :",jurusan)
print("nama prodi :",nama_jurusan)
print("harga :",harga)