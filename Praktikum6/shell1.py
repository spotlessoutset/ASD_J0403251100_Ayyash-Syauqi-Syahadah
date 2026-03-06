# ========================================================== 
# Shell Sort Ascending
# ==========================================================
# Nama  : Ayyash Syauqi Syahadah
# NIM   : J0403251100
# Kelas : TPL/A1
# ========================================================== 
def shellSortAscending(data):
    jumlahSublist = len(data)//2
    while jumlahSublist > 0:
        for posisiAwal in range(jumlahSublist):
            gapInsertionSort(data,posisiAwal,jumlahSublist)
        print("After increments of size",jumlahSublist,"The list is",data)
        jumlahSublist = jumlahSublist // 2

def gapInsertionSort(data,awal,gap):
    for i in range(awal+gap,len(data),gap):
        nilaiSekarang = data[i]
        posisi = i
        while posisi>=gap and data[posisi-gap]>nilaiSekarang:
            data[posisi]=data[posisi-gap]
            posisi = posisi-gap
        data[posisi]=nilaiSekarang
    
data = [54,26,93,17,77,31,44,55,20]
shellSortAscending(data)
print(data)

# Output
# [17, 20, 26, 31, 44, 54, 55, 77, 93]
