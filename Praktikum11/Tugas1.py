def createGraph(V, edges):
    # Membuat matriks 2D ukuran V x V diisi dengan angka 0
    mat = [[0 for _ in range(V)] for _ in range(V)]
    
    # Melakukan iterasi pada setiap pasangan edge (sisi) yang diberikan
    for it in edges:
        u = it[0]
        v = it[1]
        # Mengisi matriks pada baris u kolom v dengan 1
        mat[u][v] = 1
        # Karena graf tidak berarah (undirected), maka sebaliknya juga diisi 1
        mat[v][u] = 1
    return mat

if __name__ == "__main__":
    V = 4
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
    mat = createGraph(V, edges)

  #Menampilkan matriks
    print("Adjacency Matrix Representation:")
    for i in range(V):
        for j in range(V):
            print(mat[i][j], end=" ")
        print() # Pindah baris baru setelah satu baris matriks selesai
