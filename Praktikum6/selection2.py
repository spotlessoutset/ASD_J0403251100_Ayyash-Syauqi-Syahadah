# ========================================================== 
# Selection Sort Descending
# ==========================================================
# Nama  : Ayyash Syauqi Syahadah
# NIM   : J0403251100
# Kelas : TPL/A1
# ========================================================== 

def selectionSortDescending(data):
    for isiSlot in range(len(data)-1,0,-1):
        posisiMaks=0
        for lokasi in range(1,isiSlot+1):
            if data[lokasi]<data[posisiMaks]:
                posisiMaks = lokasi
        # Tukar
        temp = data[isiSlot]
        data[isiSlot] = data[posisiMaks]
        data[posisiMaks] = temp
data = [54,26,93,17,77,31,44,55,20]
selectionSortDescending(data)
print(data)

# Output:
# [93, 77, 55, 54, 44, 31, 26, 20, 17]