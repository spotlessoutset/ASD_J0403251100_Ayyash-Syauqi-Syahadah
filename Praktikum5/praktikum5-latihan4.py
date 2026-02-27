# ========================================================== 
# Latihan 4: Kombinasi Huruf 
# ========================================================== 
# Nama  : Ayyash Syauqi Syahadah
# NIM   : J0403251100
# Kelas : TPL/A1
# ==========================================================
 
def kombinasi(n, hasil=""): 
 
    if len(hasil) == n: #Pertama-tama kita mendefinisikan base case ketika panjang hasil sebanyak n;
        print(hasil) 
        return 
 
    kombinasi(n, hasil + "A")  # lalu kita panggil fungsi kombinasi() dengan variabel hasil ditambah huruf A
    kombinasi(n, hasil + "B") # lalu kita panggil fungsi kombinasi() dengan variabel hasil ditambah huruf A
 

 
kombinasi(2)
'''
Diskusi dan jelaskan: bagaimana jumlah kombinasi yang dihasilkan.

Fungsi ini mencetak string sepanjang n dengan huruf A dan B.
Jumlah kombinasi dihasilkan sebanyak 2 pangkat n karena ada 2 variabel sebanyak n dalam 1 kombinasi.
'''
