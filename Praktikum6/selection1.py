# ========================================================== 
# Selection Sort Ascending
# ==========================================================
# Nama  : Ayyash Syauqi Syahadah
# NIM   : J0403251100
# Kelas : TPL/A1
# ========================================================== 

def selectionSortAscending(data):
    for isiSlot in range(len(data)-1,0,-1):
        posisiMaks=0
        for lokasi in range(1,isiSlot+1):
            if data[lokasi]>data[posisiMaks]:
                posisiMaks = lokasi
        # Tukar
        temp = data[isiSlot]
        data[isiSlot] = data[posisiMaks]
        data[posisiMaks] = temp
data = [54,26,93,17,77,31,44,55,20]
selectionSortAscending(data)
print(data)

# Output:
# [17, 20, 26, 31, 44, 54, 55, 77, 93]