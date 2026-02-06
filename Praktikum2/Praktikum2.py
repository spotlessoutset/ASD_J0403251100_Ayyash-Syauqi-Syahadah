#Konsep ADT dan file handling

#Membuat fungsi load data dari file
nama_file = "data_mahasiswa.txt"
def baca_data(nama_file):
    data_dict = {}
    with open(nama_file,"r",encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            nim, nama, nilai = baris.split(",")
            data_dict[nim]={"nama":nama,"nilai":int(nilai)}
        return data_dict
    
#buka_data = baca_data(nama_file)
#print ("jumlah data terbaca", len(buka_data))

#Membuat fungsi menampilkan data
def tampilkan_data(data_dict):
    #membuat header tabel
    print("\n=========DAFTAR MAHASISWA=========")
    print(f"{'NIM' : <10} | {'Nama':<12} | {'Nilai':>5}")
    '''
    Mengatur lebar dan kolom untuk tampilan yang rapi 
    {'NIM' : <10} artinya nim rata kiri dengan lebar kolom l0 karakter 
   {'Nama':<12} artinya nama rata kiri dengan lebar kolom 12 karakter 
    {'Nilai':>5} artinya nilai rata kanan lebar kolom 5 
    '''
    print("-"*34) #Membuat garis

    #Menampilkan isi data
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10}|{nama:<12}|{int(nilai):>5}")
#tampilkan_data(buka_data)

#Membuat fungsi mencari data
def cari_data(data_dict):
    #pencarian data berdasarkan nim sebagai key dictionary
    #membuat input nim mahasiswa yang akan dicari
    nim_cari = input("Masukkan NIM mahasiswa yang ingin dicari: ").strip()
    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]
        print("\n=====Data Mahasiswa Ditemukan====")
        print(f"NIM : {nim_cari}")
        print(f"Nama : {nama}")
        print(f"Nilai : {nilai}")
    else:
        print("Data tidak ditemukan. Pastikan NIM yang dimasukkan benar.")
#cari_data(buka_data)

#Membuat fungsi update data
def ubah_data(data_dict):
    nim = input("Masukkan NIM mahasiswa yang ingin diubah datanya :").strip()
    if nim not in data_dict:
        print("NIM tidak ditemukan. Update dibatalkan")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru 0-100:").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")
        
    if nilai_baru<0 or nilai_baru>100:
        print("Nilai harus diantara 0 sampai 100. update dibatalkan")
    nilai_lama = data_dict[nim]["nilai"]
    
    data_dict[nim]["nilai"] = nilai_baru
    print(f"Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")
#ubah_data(buka_data)

#Membuat fungsi menyimpan data pada file
def simpan_data(nama_file,data_dict):

    with open (nama_file,"w",encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")
#simpan_data(nama_file,buka_data)
#print("\nData Berhasil Disimpan ke file", nama_file)

#membuat Menu
def main():
    #load data otomatis saat program dimulai
    buka_data = baca_data(nama_file)
    while True:
        print("\n=====MENU DATA MAHASISWA=====")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Berdasarkan NIM")
        print("3. Ubah Nilai Mahasiswa")
        print("4. Simpan Dara ke File")
        print("0. Keluar")

        pilihan = input("Pilih Menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan == "3":
            ubah_data(buka_data)
        elif pilihan =="4":
            simpan_data(nama_file,buka_data)
            print("Data Berhasil Disimpan")
        elif pilihan =="0":
            print("Program Selesai")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
