# ========================================================== 
# Shell Sort Descending
# ==========================================================
# Nama  : Ayyash Syauqi Syahadah
# NIM   : J0403251100
# Kelas : TPL/A1
# ========================================================== 
def shellSortDescending(data):
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
        while posisi>=gap and data[posisi-gap]<nilaiSekarang:
            data[posisi]=data[posisi-gap]
            posisi = posisi-gap
        data[posisi]=nilaiSekarang
    
data = [54,26,93,17,77,31,44,55,20]
shellSortDescending(data)
print(data)

# Output
# [93, 77, 55, 54, 44, 31, 26, 20, 17
