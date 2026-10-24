produk_bulanan ={
    "nama produk":"mie goreng",
    "harga":5000,
    "stok":14,
    "kategori":"makanan",
}
total = produk_bulanan["harga"] * 4
print("total harga:", total)

for key,veleu in produk_bulanan.items():
 print(key, ".", veleu)