# ========================================================== 
# Latihan 3: Mencari Nilai Maksimum 
# ========================================================== 
# Nama  : Ayyash Syauqi Syahadah
# NIM   : J0403251100
# Kelas : TPL/A1
# ==========================================================
 
def cari_maks(data, index=0): 
 
    # Base case 
    if index == len(data) - 1:  #Jika indeks sudah mencapai panjang data
        return data[index] # kembalikan nilai data ke-index
 
    # Recursive case 
    maks_sisa = cari_maks(data, index + 1) 
 
    if data[index] > maks_sisa: #Jika data ke-indeks lebih besar dari maks_sisa
        return data[index]  # Kembalikan nilai data ke-indeks
    else: 
        return maks_sisa # Jika tidak, kembalikan nilai maks_sisa
 
 
angka = [3, 7, 2, 9, 5] 
print("Nilai maksimum:", cari_maks(angka)) 
"""
Diskusi dan jelaskan alur program serta base case dan recursive call.

Pertama-tama kita membuat base case, yaitu ketika index sudah mencapai banyak data maka kita kembalikan nilai data ke-index.
Lalu kita menginisialisasi variabel maks_sisa dengan nilai pemanggilan fungsi cari_maks dengan index + 1.
Lalu kita cek jika data ke-index lebih besar dari maks_sisa, maka kembalikan nilai data ke-index.
Jika tidak, maka kembalikan nilai maks_sisa.

"""
