# ========================================================== 
# Insertion Sort Ascending
# ==========================================================
# Nama  : Ayyash Syauqi Syahadah
# NIM   : J0403251100
# Kelas : TPL/A1
# ========================================================== 

def insertionSortAscending(data):
    for indeks in range(1,len(data)):
        nilaiSekarang = data[indeks]
        posisi = indeks
        while posisi>0 and data[posisi-1]>nilaiSekarang:
            data[posisi]=data[posisi-1]
            posisi = posisi-1
            data[posisi]=nilaiSekarang
data = [54,26,93,17,77,31,44,55,20]
insertionSortAscending(data)
print(data)
# Output:
# [17, 20, 26, 31, 44, 54, 55, 77, 93]