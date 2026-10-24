bil = int(input("masukan jumlah anak ayam :"))
print("tek kotek kotek kotek, anak ayam turun berkotek")
if bil >=2:
    while bil>1:
        print(f"anak ayam turunlah {bil} mati satu tinggallah {bil-1}")
        bil = bil -1
        if bil<=1:
            print(f"anak ayam turunlah {bil} mati satu tinggallah {bil-1}")
else:
    print(f"anak ayam turunlah {bil} mati satu tinggal induknya")