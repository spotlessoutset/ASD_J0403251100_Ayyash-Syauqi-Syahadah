# ========================================================== 
# Quick Sort Descending
# ==========================================================
# Nama  : Ayyash Syauqi Syahadah
# NIM   : J0403251100
# Kelas : TPL/A1
# ========================================================== 

def quickSortDescending(data):
    quickSortDescendingHelper(data,0,len(data)-1)

def quickSortDescendingHelper(data,awal,akhir):
    if awal<akhir:
        splitpoint = partition(data,awal,akhir)
        quickSortDescendingHelper(data,awal,splitpoint-1)
        quickSortDescendingHelper(data,splitpoint+1,akhir)

def partition(data,awal,akhir):
    nilaiPivot = data[awal]
    penandaKiri = awal+1
    penandaKanan = akhir
    selesai = False
    while not selesai:
        while penandaKiri <= penandaKanan and data[penandaKiri] >= nilaiPivot:
            penandaKiri = penandaKiri + 1
        while data[penandaKanan] <= nilaiPivot and penandaKanan >= penandaKiri:
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
quickSortDescending(data)
print(data)

# Output
# [93, 77, 55, 54, 44, 31, 26, 20, 17]