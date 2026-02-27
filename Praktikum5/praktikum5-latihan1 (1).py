# ========================================================== 
# Latihan 1: Rekursi Pangkat 
# ========================================================== 
# Nama  : Ayyash Syauqi Syahadah
# NIM   : J0403251100
# Kelas : TPL/A1
# ==========================================================

def pangkat(a, n):  # Mendefinisikan fungsi pangkat dengan variabel a(basis) dan n(pangkat)
    # Base case 
    if n == 0: # Jika n bernilai 0 
        return 1  # Maka kembalikan nilai 1
    '''
     Penjelasan: Base case pada fungsi ini adalah untuk memberhentikan fungsi rekursif ketika n(pangkat) bernilai 0 
     dan mengembalikan nilai 1 karena berapapun nilai a(basis) jika dipangkatkan 0, maka bernilai 1
    '''
    # Recursive case 
    return a * pangkat(a, n - 1)  # Kembalikan nilai a dikali fungsi pangkat() dengan variabel n dikurangi 1
    '''
    Penjelasan: Recursive case pada fungsi ini adalah untuk mengalikan a(basis) dengan 
    fungsi pangkat() yang nilai n(pangkat) dikurangi 1 pada setiap pemanggilannya sehingga dapat mencapai base case(n=0) 
    '''
print(pangkat(2, 4))  # Output: 16
     
'''
Diskusi dan jelaskan alur program serta base case dan recursive call.

Alur: Pertama-tama kita harus mendefinisikan base case yaitu ketika nilai n bernilai 0.
Lalu kita mengalikan a(basis) dengan fungsi pangkat() dengan n dikurangi 1 agar mencapai base case.
Jadi, program ini adalah mengalikan a(basis) sebanyak n(pangkat)
'''