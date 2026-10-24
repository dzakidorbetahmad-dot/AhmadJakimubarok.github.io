print ("HITUNG GRADE")
nilai = int(input("MASUKAN NILAI:"))
if (nilai > 100):
    grade = "over"
elif (nilai <=100) and (nilai >= 80):
    grade = "a"
elif (nilai >= 69) and (nilai <= 79):
    grade = "b"
elif (nilai >= 56) and (nilai <= 68):
    grade = "c"
elif (nilai >= 45) and (nilai <= 55):
    grade = "d"
elif (nilai >= 0) and (nilai <= 45):
    garde = "e"
elif (nilai < 0):
    grade = "minor"
else :
    grade = "tidak di ketahui"
    
print("NILAI GRADE =",grade)