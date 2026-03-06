# ========================================================== 
# Bubble Sort Descending
# ==========================================================
# Nama  : Ayyash Syauqi Syahadah
# NIM   : J0403251100
# Kelas : TPL/A1
# ========================================================== 
 
def bubbleSortDescending(data):
    for batas in range(len(data)-1,0,-1):
        for i in range(batas):
            if data[i]<data[i+1]:
                # Tukar dua data bersebelahan yang urutannya salah
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp
data = [54,26,93,17,77,31,44,55,20]
bubbleSortDescending(data)
print(data)
# Output
# [93, 77, 55, 54, 44, 31, 26, 20, 17]
