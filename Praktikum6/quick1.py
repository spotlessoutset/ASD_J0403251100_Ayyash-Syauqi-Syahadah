# ========================================================== 
# Quick Sort Ascending
# ==========================================================
# Nama  : Ayyash Syauqi Syahadah
# NIM   : J0403251100
# Kelas : TPL/A1
# ========================================================== 

def quickSortAscending(data):
    quickSortAscendingHelper(data,0,len(data)-1)

def quickSortAscendingHelper(data,awal,akhir):
    if awal<akhir:
        splitpoint = partition(data,awal,akhir)
        quickSortAscendingHelper(data,awal,splitpoint-1)
        quickSortAscendingHelper(data,splitpoint+1,akhir)

def partition(data,awal,akhir):
    nilaiPivot = data[awal]
    penandaKiri = awal+1
    penandaKanan = akhir
    selesai = False
    while not selesai:
        while penandaKiri <= penandaKanan and data[penandaKiri] <= nilaiPivot:
            penandaKiri = penandaKiri + 1
        while data[penandaKanan] >= nilaiPivot and penandaKanan >= penandaKiri:
            penandaKanan = penandaKanan-1
        if penandaKanan < penandaKiri:
            selesai = True
        else:
            temp = data[penandaKiri]
            data[penandaKiri] = data[penandaKanan]
            data[penandaKanan] = temp
    temp = data[awal]
    data[awal] = data[penandaKanan]
    data[penandaKanan] = temp
    return penandaKanan
data = [54,26,93,17,77,31,44,55,20]
quickSortAscending(data)
print(data)

# Output
# [17, 20, 26, 31, 44, 54, 55, 77, 93]