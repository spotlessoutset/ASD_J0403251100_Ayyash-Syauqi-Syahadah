#==================================
#Nama : Ayyash Syauqi Syahadah
#NIM : J0403251100
#Kelas : TPL A1
#==================================
#==========================================
#Implementasi Dasar: Node pada Linked List
#==========================================
class Node:
    def __init__ (self,data):
        self.data = data #menyimpan data pada list
        self.next = None #pointer menunjuk ke node berikutnya

#1) membuat node dengan instantiasi class node
nodeA=Node("A")
nodeB=Node("B")
nodeC=Node("C")

#2) Menguhubungkan Node : A->B->C->None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#4)Traversal : Menelusuri node dari head sampai ke None
current = head
while current is not None:
    print(current.data)#menampilkan data pada node saat ini
    current = current.next#pindah ke node berikutnya
