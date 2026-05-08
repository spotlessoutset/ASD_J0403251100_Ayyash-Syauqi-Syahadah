def createGraph(V, edges):
    adj = [[] for _ in range(V)]
    
    # Menambahkan setiap edge ke adjacency list
    for it in edges:
        u = it[0]
        v = it[1]
        adj[u].append(v)
        
    return adj

if __name__ == "__main__":
    # Daftar nama untuk referensi saat mencetak
    names = ["Andi", "Budi", "Citra", "Dinda", "Eko"]
    V = len(names)

    # List of edges berdasarkan hubungan yang diberikan
    edges = [
        [0, 1], [1, 0], [0, 2], 
        [1, 3], [2, 3], [4, 1], [2, 1]
    ]

    # Membangun graf
    adj = createGraph(V, edges)

    print("Adjacency List Representation:")
    for i in range(V):
        # Mencetak nama vertex
        print(f"{names[i]}:", end=" ")
        for j in adj[i]:
            # Mencetak nama tetangganya
            print(names[j], end=" ")
        print()
