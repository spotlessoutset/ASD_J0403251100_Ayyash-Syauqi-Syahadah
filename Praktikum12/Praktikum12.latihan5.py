import heapq

# Graph berbobot: setiap node memetakan ke dictionary tetangga dan bobotnya
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

def dijkstra(graph, start): 
    """ 
    Fungsi untuk mencari jarak terpendek dari node start 
    ke seluruh node lain menggunakan algoritma Dijkstra. 
    """ 
    # Semua jarak awal dibuat tak hingga 
    distances = {node: float('inf') for node in graph} 
    # Jarak dari start ke start adalah 0 
    distances[start] = 0 
    # Priority queue menyimpan pasangan (jarak, node) 
    priority_queue = [(0, start)]
    while priority_queue: 
        current_distance, current_node = heapq.heappop(priority_queue) 

        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat, 
        # maka proses dilewati 
        if current_distance > distances[current_node]: 
            continue 

        # Periksa semua tetangga dari node saat ini 
        for neighbor, weight in graph[current_node].items(): 
            distance = current_distance + weight 

            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya 
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                heapq.heappush(priority_queue, (distance, neighbor)) 
    return distances 
    
 
hasil = dijkstra(graph, 'Bogor') 
 
print("Jarak terpendek dari node Bogor:") 
for node, distance in hasil.items(): 
    print(node, "=", distance) 

# Jawaban Analisis: 
# 1. Node awal yang digunakan apa? 
# Node awal yang digunakan adalah Bogor.

# 2. Node mana yang memiliki jarak paling kecil dari node awal? 
# Node yang memiliki jarak paling kecil dari Bogor adalah Depok dengan jarak 2.

# 3. Node mana yang memiliki jarak paling besar dari node awal? 
# Node yang memiliki jarak paling besar dari Bogor adalah Bandung dengan jarak 7.

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
# Algoritma Dijkstra bekerja dengan memulai dari node Bogor dan menginisialisasi jarak ke semua node lain sebagai tak hingga, kecuali jarak ke node awal itu sendiri yang diinisialisasi menjadi 0.
# Algoritma kemudian menggunakan priority queue untuk selalu memproses node dengan jarak terpendek yang diketahui saat ini.
# Untuk setiap node yang diproses, algoritma memeriksa tetangganya dan memperbarui jarak jika ditemukan jalur yang lebih pendek melalui node tersebut. 
# Proses ini berlanjut hingga semua node telah diproses, menghasilkan jarak terpendek dari node awal ke semua node lain dalam graph.
