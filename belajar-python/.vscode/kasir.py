from test import tampil_toko


def hitung_total(pesanan):
    total = 0
    for nama, jumlah, harga in pesanan:
        total += jumlah * harga
    return total


def kasir():
    tampil_toko()
    print("\n==== PROGRAM KASIR ====")

    pesanan = []

    while True:
        nama = input("Masukkan nama barang: ").strip()
        if not nama:
            print("Nama barang tidak boleh kosong.")
            continue

        try:
            jumlah = int(input(f"Jumlah {nama}: "))
            harga = int(input(f"Harga satuan {nama}: Rp "))
        except ValueError:
            print("Jumlah dan harga harus angka.")
            continue

        pesanan.append((nama, jumlah, harga))

        lanjut = input("Tambah barang lain? (y/n): ").strip().lower()
        if lanjut != 'y':
            break

    if not pesanan:
        print("Tidak ada barang yang dibeli.")
        return

    total = hitung_total(pesanan)

    print("\n=== STRUK BELANJA ===")
    for nama, jumlah, harga in pesanan:
        subtotal = jumlah * harga
        print(f"{nama} x {jumlah} = Rp {subtotal}")

    print(f"\nTotal: Rp {total}")

    try:
        uang = int(input("Uang yang dibayar: Rp "))
    except ValueError:
        print("Uang harus angka.")
        return

    kembalian = uang - total

    if kembalian >= 0:
        print(f"Kembalian: Rp {kembalian}")
    else:
        print(f"Uang kurang: Rp {abs(kembalian)}")

    print("\nTerima kasih sudah belanja di sini.")


if __name__ == '__main__':
    kasir()