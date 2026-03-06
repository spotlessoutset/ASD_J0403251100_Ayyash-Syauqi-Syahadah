# ========================================================== 
# Insertion Sort Descending
# ==========================================================
# Nama  : Ayyash Syauqi Syahadah
# NIM   : J0403251100
# Kelas : TPL/A1
# ========================================================== 

def insertionSortDescending(data):
    for indeks in range(1,len(data)):
        nilaiSekarang = data[indeks]
        posisi = indeks
        while posisi>0 and data[posisi-1]<nilaiSekarang:
            data[posisi]=data[posisi-1]
            posisi = posisi-1
            data[posisi]=nilaiSekarang
data = [54,26,93,17,77,31,44,55,20]
insertionSortDescending(data)
print(data)
# Output:
# [93, 77, 55, 54, 44, 31, 26, 20, 17]