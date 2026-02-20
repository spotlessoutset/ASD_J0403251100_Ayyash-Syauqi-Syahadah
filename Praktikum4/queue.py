#==================================
#Nama : Ayyash Syauqi Syahadah
#NIM : J0403251100
#Kelas : TPL A1
#==================================
#==========================================
#Implementasi Dasar: Queue
#==========================================
class Node:
    def __init__ (self,data):
        self.data = data #menyimpan data pada list
        self.next = None #pointer menunjuk ke node berikutnya

class queue:
    def __init__(self):
        self.front = None #node paling depan bernilai None
        self.rear = None #node paling belakang bernilai None
    
    def is_empty(self):
        return self.front is None
    
    #menambah data baru di belakang
    def enqueue(self,data):
        nodeBaru = Node(data)

        if self.is_empty():
            self.front=nodeBaru
            self.rear=nodeBaru
            return
        self.rear.next=nodeBaru #letakkan data baru setelah rear
        self.rear = nodeBaru #Jadikan data baru sebagai rear

    def dequeue(self):
        data_terhapus = self.front.data #lihat data paling depan
        self.front=self.front.next#Geser ke font berikutnya
        if self.front is None: #Jika di depan bernilai None, maka belakang juga None
            self.rear = None
        return data_terhapus #Kembalikan nilai data_terhapus

    def tampilkan(self):
        #Menampilkan data dengan format Front->A->B->Rear
        current = self.front
        print("Front->" , end=" ")
        while current is not None:
            print(current.data,end="->")
            current = current.next
        print("Rear")

q = queue()
q.enqueue("A")
q.enqueue("B")
q.tampilkan()
q.dequeue()
q.tampilkan()
