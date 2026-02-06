print("---Membuka file dalam satu string---")
with open("data_mahasiswa.txt", "r",encoding="utf-8") as file:
    isi_file = file.read()
    print(isi_file)

print("\n---Membuka file per baris---")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r",encoding="utf-8") as file:
    for baris in file:
        jumlah_baris +=1 # Membuat Indeks
        baris = baris.strip() # Menghapus \n (baris baru)
        print("Baris", jumlah_baris)
        print("Isinya: ", baris)
        
#memecah baris menjadi beberapa data dan ditampilkan dengan kolom
with open("data_mahasiswa.txt", "r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() # Menghapus \n (baris baru)
        nim,nama,nilai = baris.split(",")
        print("NIM :", nim,"| Nama :",nama,"| Nilai :", nilai)
        
   
data_list = [] #inisialisasi list
with open("data_mahasiswa.txt", "r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() # Menghapus \n (baris baru)
        nim,nama,nilai = baris.split(",")
        data_list.append([nim,nama,int(nilai)])

print("---Menampilkan list---")
print(data_list)
print("Data ke-1:",data_list[0])
print("Jumlah record :", len(data_list))

data_dict = {}
with open("data_mahasiswa.txt", "r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() # Menghapus \n (baris baru)
        nim,nama,nilai = baris.split(",")
        #simpan data dalam dictionary
        data_dict[nim] = {
            "nama": nama,
            "nilai":int(nilai)
        }
        
    print(data_dict)