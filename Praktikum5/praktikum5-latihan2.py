# ========================================================== 
# Latihan 2: Tracing Rekursi 
# ==========================================================
# Nama  : Ayyash Syauqi Syahadah
# NIM   : J0403251100
# Kelas : TPL/A1
# ==========================================================

def countdown(n): 
    
    #Base case
    if n == 0: # Jika n adalah 0
        print("Selesai")  # Maka print selesai
        return # Keluar dari fungsi tanpa mengembalikan nilai
 
    print("Masuk:", n)  # Cetak nilai n dengan awalan "Masuk:"
    
    #Recursive case
    countdown(n - 1) # Memanggil fungsi countdown() dengan n dikurangi 1
 
    print("Keluar:", n) # Cetak nilai n dengan awalan "Keluar:"
 
 
countdown(3) 

'''
Diskusi dan jelaskan: Mengapa output 'Keluar' muncul terbalik?

Karena output "keluar" dicetak setelah pemanggilan fungsi countdown() yang telah 
mencapai base case sehingga mencetak output dari n terkecil(karena telah dikurangi setiap pemanggilan) hingga terbesar
'''
