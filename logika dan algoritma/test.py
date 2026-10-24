N = int(input("masukan bilangan bulat (1-100) :"))
if 1<= N <= 100:
    for i in range(1,N +1):
        for j in range(i):
            print("*",end="")
        print()
else:
    print("masukan tidak valid.harapkan masukan bilangan antara 1 dan 99.")
    
    
    
bil = int(input("masukan jumlah perulangan :"))
kar = input("masukan karakter :")
s = bil - 1
for i in range(0, bil):
    for j in range(0,s):
        print(' ', end='')
    s -= 1
    for j in range(0, i + 1):
        print(kar, end=' ')
    print('')