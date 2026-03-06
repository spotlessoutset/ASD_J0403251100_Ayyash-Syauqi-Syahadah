# ========================================================== 
# Soal Pak Budi
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

data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
dict = {}

for i in range(len(data)):
    dict.update({data[i]:i+1})
bubbleSortDescending(data)
print("Nilai-nilai dari 5 kandidat tertinggi adalah",data[:5])

print("kandidat yang lolos adalah kandidat")
for i in range(5):
    if i==4:
        print(" dan ",end="")
    print("ke-",dict[data[i]],end="")
    if i != 4:
        print(",",end="")
    

