class	Node:	
    def	__init__(self,	data):	
        self.data	=	data	
        self.next	=	None	
class	CircularSinglyLinkedList:	
    def	__init__(self):	
        self.head	=	None	
        self.tail	=	None		#	Tambahkan	pointer	tail	
    def	insert_at_end(self,	data):	
        new_node	=	Node(data)	
        if	not	self.head:		#	Jika	linked	list	kosong	
            self.head	=	new_node	
            self.tail	=	new_node	
            self.tail.next	=	self.head		#	Circular	link	ke	dirinya	sendiri	
        else:	
            self.tail.next	=	new_node		#	Sambungkan	tail	ke	node	baru	
            self.tail	=	new_node		#	Update	tail	ke	node	baru	
            self.tail.next	=	self.head		#	Circular	link	kembali	ke	head	
        
    def	display(self):
        if	not	self.head:	
            print("List	is empty")	
            return	
        print("Circular Linked List Traversal:")	
        temp	=	self.head	
        print(temp.data,	end=" -> ")	
        temp	=	temp.next	
        while	temp	!=	self.head:	
            print(temp.data,	end=" -> ")	
            temp	=	temp.next	
        print("... (back to head)")	
    def search(self, key): 
        temp = self.head 
        while temp: 
            if temp.data == key: 
                return True 
            temp = temp.next 
        return False 

cll	=	CircularSinglyLinkedList()	
elemen=input("Masukkan Elemen ke dalam Circular Linked List(Pisahkan dengan Koma):")
elemen=elemen.strip()
elemen=elemen.split(",")
jumlahElemen=len(elemen)
for i in range(jumlahElemen):
    cll.insert_at_end(int(elemen[i]))	
cll.display()	
elemenDicari=int(input("Masukkan Elemen yang Ingin Dicari:"))
statusDicari = cll.search(elemenDicari)
if jumlahElemen==0:
    print("Circular Linked List Kosong. Tidak Ada Elemen yang Bisa Dicari.")
elif statusDicari == True:
    print("Elemen",elemenDicari,"Ditemukan dalam Circular Linked List")
elif statusDicari==False:
    print("Elemen",elemenDicari,"TIDAK Ditemukan dalam Circular Linked List")
