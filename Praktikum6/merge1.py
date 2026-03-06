# ========================================================== 
# Merge Sort Ascending
# ==========================================================
# Nama  : Ayyash Syauqi Syahadah
# NIM   : J0403251100
# Kelas : TPL/A1
# ========================================================== 

def mergeSortAscending(data):
    print("Splitting ",data)
    if len(data)>1:
        tengah = len(data)//2
        kiri = data[:tengah]
        kanan = data[tengah:]
        mergeSortAscending(kiri)
        mergeSortAscending(kanan)
        i=0
        j=0
        k=0
        while i < len(kiri) and j < len(kanan):
            if kiri[i] <= kanan[j]:
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
mergeSortAscending(data)
print(data)

# Output:
# [17, 20, 26, 31, 44, 54, 55, 77, 93]