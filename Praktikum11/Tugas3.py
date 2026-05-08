# Definisi manual adjacency matrix
matrix = [
    [0, 1, 1, 0], # Node 0 bertetangga dengan 1 dan 2
    [1, 0, 1, 0], # Node 1 bertetangga dengan 0 dan 2
    [1, 1, 0, 1], # Node 2 bertetangga dengan 0, 1, dan 3
    [0, 0, 1, 0]  # Node 3 bertetangga dengan 2
]

# Inisialisasi dictionary kosong untuk menyimpan list
adj_list = {}

# Proses konversi baris demi baris
for i in range(len(matrix)):
    # Membuat entry list kosong untuk setiap index i
    adj_list[i] = []

    # Mengecek setiap kolom j di baris i
    for j in range(len(matrix[i])):
        # Jika nilai pada matriks adalah 1, berarti ada koneksi
        if matrix[i][j] == 1:
            # Masukkan index j ke dalam list tetangga node i
            adj_list[i].append(j)

# Menampilkan hasil akhir
print("Adjacency List:\n")
for node in adj_list:
    # Contoh output: 0 -> [1, 2]
    print(f"{node} -> {adj_list[node]}")
