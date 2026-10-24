daftar_pesanan = []
total_belanja = 0

welcome_mesege = 'daftar menu'
print("==========================================")
print("      selamat datng di nasgor bangjago    ")
print("==========================================")
print("==========================================")
print(f"halo.. silahkan pilih menu dari {welcome_mesege} tersebut")
print("1.nasi goreng  :  Rp : 15.000")
print("2.es teh manis :  RP : 6.000 ")
print("==========================================")


# 2. bagian II
while True:
    pilihan_user = input("\n silahkan ketik (1/2) atau keti 'x' untuk akhiri pesanan ")
    
    if pilihan_user.lower() == 'x': 
        break 
    
    if pilihan_user == "1":
        nama_barang = "nasi goreng"
        harga = 15000
    elif pilihan_user == "2":
        nama_barang = "es teh manis"
        harga = 7000 
    else :
        print ("pilihan menu tida ada disini")
        continue 
    
    jumlah = int(input(f"beli berapa porsi {nama_barang}"))
    subtotal = harga * jumlah
    total_belanja += subtotal
    
    daftar_pesanan.append(f"{nama_barang} ({jumlah} porsi) - RP {subtotal}")
    print (f" -> berhasil menambahkan {nama_barang} kedaftar belanja." )
 
    if total_belanja == 0:
     print("\n tidak ada transaksi di aktifkan terima kasih")
    else 
        