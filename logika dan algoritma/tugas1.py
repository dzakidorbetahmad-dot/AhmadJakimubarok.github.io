gp = int(input(""))
jk = int(input(""))
tjg = 20/100 * gp

if (jk > 200):
    tambahan = 20000 + (200-jk)
else :
    tambahan = 0
    
pajak = 10/100 * gp

print("gaji poko :",gp)
print("jam kerja :",jk)
print("tunjangan :",tjg)
print("tambahan :",tambahan)
print("pajak :",pajak)
gaji_kotor = gp + tjg + jk - pajak
print("gaji kotor",gaji_kotor)
