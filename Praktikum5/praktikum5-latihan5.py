# ========================================================== 
# Studi Kasus: Generator PIN 
# ==========================================================
# # Nama  : Ayyash Syauqi Syahadah
# NIM   : J0403251100
# Kelas : TPL/A1
# ========================================================== 
 
def buat_pin(panjang, hasil=""): 
 
    if len(hasil) == panjang: # Jika panjang hasil telah mencapai panjang
        print("PIN:", hasil)  # Cetak hasil 
        return 
 
    for angka in ["0", "1", "2"]:# Pada setiap angka pada array ["0", "1", "2"] ulangi
        buat_pin(panjang, hasil + angka) # panggil fungsi dengan variabel hasil ditambah angka
 
 
buat_pin(3)
'''
Diskusi dan jelaskan: Bagaimana cara mencegah angka yang sama muncul berulang?

Cara program ini mencegah angka yang sama muncul berulang adalah dengan mengecek 
jika angka sebelumnya sudah digunakan maka jangan kembalikan nilai apa-apa.
'''
