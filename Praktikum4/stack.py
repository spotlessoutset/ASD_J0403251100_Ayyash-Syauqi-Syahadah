#==================================
#Nama : Ayyash Syauqi Syahadah
#NIM : J0403251100
#Kelas : TPL A1
#==================================
#==========================================
#Implementasi Dasar: Stack
#==========================================
class Node:
    def __init__ (self,data):
        self.data = data #menyimpan data pada list
        self.next = None #pointer menunjuk ke node berikutnya

class stack:
    def __init__(self):
        self.top = None

    #Jika tidak ada, kembalikan None
    def is_empty(self):
        return self.top is None
    
    def push(self,data):
        #membuat node baru
        nodeBaru = Node(data)

        #node baru harus menunjuk ke top yang lama
        nodeBaru.next = self.top

        #geser top pindah ke node baru
        self.top = nodeBaru

    def peek(self):
        #melihat data paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data

    def pop(self):
            #mengambil/menghapus node paling atas
            if self.is_empty():
                print("Stack Kosong, tidak bisa pop")
                return None
            data_terhapus = self.top.data
            self.top=self.top.next
            return data_terhapus
    
    def tampilkan(self):
        #Menampilkan data dengan format Top->A->B
        current = self.top
        print("Top->" , end=" ")
        while current is not None:
            print(current.data,end="->")
            current = current.next
        print("None")

s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
s.pop()
s.tampilkan()
