# ulang =2 
# for i in range(ulang):
#     print("DATA KE -",(i + 1))
#     nama = input("masukan Nim anda :")
#     uts = int(input("masukan nilai uts :"))
#     uas = int(input("masukan nilai uas :"))
#     print("Nim anda adalah %s nilai uts anda adalah %i niali uas anda adalah %i" % (nama,uts,uas))
#     # print(f"Nim anda adalah {nama} nilai uts anda adalah {uts} niali uas anda adalah {uas}")
#     print("-" * 35)
    
    

# banyak_jenis = input

# Daftar harga
# Program Kasir Gerobak Fried Chicken

# Daftar menu
menu = {
    'D': {'nama': 'Dada', 'harga': 2500},
    'P': {'nama': 'Paha', 'harga': 2000},
    'S': {'nama': 'Sayap', 'harga': 1500}
}

keranjang = []
subtotal = 0

print("=" * 40)
print("   GEROBAK FRIED CHICKEN")
print("=" * 40)

while True:
    kode = input("Masukkan kode potong (D/P/S) atau X untuk selesai: ").upper()

    if kode == 'X':
        break

    if kode not in menu:
        print("Kode tidak valid!")
        continue

    jumlah = int(input(f"Masukkan jumlah {menu[kode]['nama']} : "))

    harga_satuan = menu[kode]['harga']
    total_item = harga_satuan * jumlah

    keranjang.append({
        'kode': kode,
        'nama': menu[kode]['nama'],
        'harga': harga_satuan,
        'jumlah': jumlah,
        'total': total_item
    })

    subtotal += total_item

print("\n" + "=" * 40)
print("      STRUK PEMBELIAN")
print("=" * 40)

for item in keranjang:
    print(f"{item['nama']:<10} {item['jumlah']:>3} x {item['harga']:>6} = Rp {item['total']:>8}")

pajak = 0.10 * subtotal
total_akhir = subtotal + pajak

print("-" * 40)
print(f"Subtotal      : Rp {subtotal:>8}")
print(f"Pajak 10%     : Rp {pajak:>8}")
print(f"Total Bayar   : Rp {total_akhir:>8}")

uang = int(input("Uang Pembeli : Rp "))

kembalian = uang - total_akhir
print(f"Kembalian    : Rp {kembalian:>8}")
print("=" * 40)