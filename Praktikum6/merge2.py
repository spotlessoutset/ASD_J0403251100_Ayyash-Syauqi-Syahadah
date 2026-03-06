# ========================================================== 
# Merge Sort Descending
# ==========================================================
# Nama  : Ayyash Syauqi Syahadah
# NIM   : J0403251100
# Kelas : TPL/A1
# ========================================================== 

def mergeSortDescending(data):
    print("Splitting ",data)
    if len(data)>1:
        tengah = len(data)//2
        kiri = data[:tengah]
        kanan = data[tengah:]
        mergeSortDescending(kiri)
        mergeSortDescending(kanan)
        i=0
        j=0
        k=0
        while i < len(kiri) and j < len(kanan):
            if kiri[i] >= kanan[j]:
                data[k]=kiri[i]
                i=i+1
            else:
                data[k]=kanan[j]
                j=j+1
            k=k+1
        while i < len(kiri):
            data[k]=kiri[i]
            i=i+1
            k=k+1
        while j < len(kanan):
            data[k]=kanan[j]
            j=j+1
            k=k+1
        print("Merging ",data)
data = [54,26,93,17,77,31,44,55,20]
mergeSortDescending(data)
print(data)

# Output:
# [93, 77, 55, 54, 44, 31, 26, 20, 17]