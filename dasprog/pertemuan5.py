# # lis_number 
# number = [7,5,9,8,9,0,8,4,0]

# # variabel untuk menyimpan jumlah
# sum = 0

# # iterasi
# for each in number:
#     sum = sum + each
# print("JUMLAH SEMUANYA",sum)


# count = 0 
# while (count < 5 ):
#     print(count,'kurang dari 5')
#     count = count + 1
# else:
#     print(count,"tidak kurang dari 5")
# print('selesai')


# for later in 'pythonprograming':
#     if later == 'g':
#         break
#     print("huruf sekarang",later)
# print("good bye")
# for later in 'pythonprograming':
#     if later == 'g':
#         continue
#     print("huruf sekarang",later)
# print("good bye")



# TUGAS BUAT KASIR FRIED CICKEN
# harga = {"1": 2500, "2": 2000 , "3": 1500}
# jenis = {"1": "dada", "2": "paha", "3": "sayap"}

# total = 0

# banyak_jenis = int(input("masukan jenis :"))

# for i in range(banyak_jenis):
#     print(f"\nData ke-{i + 1}")
#     kode = input('''
# jenis potongan
# 1.dada
# 2.paha
# 3.sayap
# silahkan pilih kategori di atas ini:''')  
#     if kode in jenis:
#         print(kode)
#         jadi = jenis 
#     else:
#         print("maaf hanya boleh masukan yang di atas!")
#         exit(kode)
    
#     banyak_beli = int(input("BANYAK BELI :"))

#     if kode in jenis:
#         subtotal = jenis * banyak_beli
#         total = subtotal
#         print(f"{jenis} RP. {harga} * {banyak_beli} = RP. {subtotal}")
#     else:
#         print("kode tidak di kenal")
        
# pajak = total * 0.10
# bayar = total + pajak

# print("\n-----------------------")
# print(f"Total   : Rp. {total}")
# print(f"Pajak 10%: Rp. {pajak}")
# print(f"Total Bayar: Rp. {bayar}")


# Daftar harga: kode -> (nama potong, harga)
menu = {
    "D": ("Dada", 2500),
    "P": ("Paha", 2000),
    "S": ("Sayap", 1500),
}

# Layar Masukkan
print("GEROBAK FRIED CHICKEN")
print("-" * 30)
print("Kode  JenisPotong  Harga")
print("-" * 30)
for kode, (nama, harga) in menu.items():
    print(f"{kode:<6}{nama:<13}Rp. {harga}")
print("-" * 30)

banyak_jenis = int(input("Banyak Jenis      : "))

pesanan = []
for i in range(1, banyak_jenis + 1):
    print(f"Jenis Ke - {i}")
    kode = input("Kode Potong [D/P/S]: ").upper()
    while kode not in menu:
        print("Kode tidak valid, ulangi.")
        kode = input("Kode Potong [D/P/S]: ").upper()
    banyak = int(input("Banyak Potong     : "))

    nama, harga = menu[kode]
    pesanan.append((i, nama, harga, banyak, harga * banyak))

# Layar Keluaran
jumlah_bayar = sum(p[4] for p in pesanan)
pajak = jumlah_bayar * 10 / 100
total_bayar = jumlah_bayar + pajak

print()
print("GEROBAK FRIED CHICKEN")
print("-" * 52)
print(f"{'No.':<5}{'Jenis Potong':<14}{'Harga Satuan':<14}{'Bayak Beli':<12}{'Jumlah Harga'}")
print("-" * 52)
for no, nama, harga, banyak, jumlah in pesanan:
    print(f"{no:<5}{nama:<14}{harga:<14}{banyak:<12}Rp {jumlah}")
print("-" * 52)
print(f"{'Jumlah Bayar':>38} Rp {jumlah_bayar}")
print(f"{'Pajak 10%':>38} Rp {pajak:.0f}")
print(f"{'Total Bayar':>38} Rp {total_bayar:.0f}")
