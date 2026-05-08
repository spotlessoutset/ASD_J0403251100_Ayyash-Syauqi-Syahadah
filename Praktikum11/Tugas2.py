def createGraph(V, edges):
    # Membuat list berisi V buah list kosong
    adj = [[] for _ in range(V)]
    
    for it in edges:
        u = it[0]
        v = it[1]
        # Menambahkan v ke daftar tetangga u
        adj[u].append(v)
        # Menambahkan u ke daftar tetangga v (graf tidak berarah)
        adj[v].append(u)
    return adj

if __name__ == "__main__":
    # Mapping: 0=A, 1=B, 2=C, 3=D
    names = ["A", "B", "C", "D"]
    V = len(names)
    
    # List of edges (menggunakan angka indeks)
    edges = [[0, 1], [1, 3], [3, 2], [2, 0]]
    
    # Membuat Graf
    adj = createGraph(V, edges)
    
    # Menampilkan list
    print("Adjacency List Representation:")
    for i in range(V):
        # Mengonversi indeks i menjadi nama (A, B, C, D)
        print(f"{names[i]}:", end=" ")
        for j in adj[i]:
            # Mengonversi indeks tetangga j menjadi nama
            print(names[j], end=" ")
        print()
