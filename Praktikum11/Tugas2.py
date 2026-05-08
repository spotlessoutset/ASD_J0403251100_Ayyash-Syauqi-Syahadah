def createGraph(V, edges):
    # Membuat list berisi V buah list kosong (satu untuk setiap vertex)
    # Catatan: 'v' kecil di kode asli harusnya 'V' besar agar sesuai parameter
    adj = [[] for _ in range(V)]
    
    for it in edges:
        u = it[0]
        v = it[1]
        # Menambahkan v ke daftar tetangga u
        adj[u].append(v)
        # Menambahkan u ke daftar tetangga v (karena graf tidak berarah)
        adj[v].append(u)
    return adj

if __name__ == "__main__":
    V = 4
    # Catatan: A, B, C, D harus didefinisikan sebagai angka (0, 1, 2, 3) 
    # atau string agar tidak error
    edges = [[0, 1], [1, 3], [3, 2], [2, 0]]
    #Membuat Graf
    adj = createGraph(V, edges)
#Menampilkan list
    print("Adjacency List Representation:")
    for i in range(V):
        print(f"{i}:", end=" ")
        for j in adj[i]:
            print(j, end="_")
        print()
