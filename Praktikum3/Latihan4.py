class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None 
class LinkedList: 
    def __init__(self): 
        self.head = None 
        self.tail = None  # Tambahkan pointer tail 
    def insert_at_end(self, data): 
        new_node = Node(data) 
        if not self.head:  # Jika linked list kosong 
            self.head = new_node 
            self.tail = new_node  # Tail juga menunjuk ke node pertama 
        else: 
            self.tail.next = new_node  # Sambungkan tail ke node baru 
            self.tail = new_node  # Update tail ke node baru 
    def display(self): 
        temp = self.head
        while temp: 
            print(temp.data, end=" -> ") 
            temp = temp.next 
        print("null")

ll = LinkedList()
ll1 = LinkedList()
ll2 = LinkedList()
input1=input("Masukkan Elemen untuk Linked List 1(Pisahkan dengan Koma):")
input2=input("Masukkan Elemen untuk Linked List 2(Pisahkan dengan Koma):")
input1=input1.strip()
input1=input1.split(",")
input2=input2.strip()
input2=input2.split(",")
jumlahElemen1=len(input1)
jumlahElemen2=len(input2)
for i in range(jumlahElemen1):
    ll1.insert_at_end(int(input1[i]))
    ll.insert_at_end(int(input1[i]))
print("Linked List 1:")
ll1.display()
print("Linked List 2:")
for i in range(jumlahElemen2):
    ll2.insert_at_end(int(input2[i]))
    ll.insert_at_end(int(input2[i]))
ll2.display()
print("Linked List Setelah Digabungkan:")
ll.display()	