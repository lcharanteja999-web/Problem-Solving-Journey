class node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next
    
class linkedlist:

    def __init__(self,head = None): 
        self.head = head


    #---------------------------creating linked list-----------------

    def create_node(self):  #creating methods to create linked list
        temp = self.head

        while True:
            choice = int(input("enter 1 to create node or 0 to stop:\n"))

            if choice == 0:
                break
            
            data = int(input("enter data for the new node:\n"))
            newnode = node(data)

            if self.head is None:  #first node
                self.head = newnode
                temp = newnode
            else:
                temp.next = newnode
                temp = temp.next

        if self.head is not None:
            temp.next = self.head
    
     #-------------------inserting at first------------------#           

    def insert_at_first(self): 
        data = int(input("enter data:\n"))

        newnode = node(data)

        if self.head is None:  #edge case for empty list
            self.head = newnode
            newnode.next = newnode
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        newnode.next = self.head
        self.head = newnode
        temp.next = newnode

    #----------------------insert at last----------------------4

    def insert_at_last(self):
        data = int(input("enter data:\n"))
        newnode = node(data)

        if self.head is None:    #egde case for empty list
            self.head = newnode
            newnode.next = newnode
            return
        
        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        temp.next = newnode
        newnode.next = self.head
    
    def insert_at_position(self):
        data = int(input("enter data:\n"))
        pos = int(input("enter position:\n"))

        newnode = node(data)

        if self.head is None:
            newnode.next = newnode
            self.head = newnode

            return
        
        if pos == 0:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next
            
            newnode.next = self.head
            temp.next = newnode
            self.head = newnode

            return
    
        temp = self.head

        for _ in range(1,pos -1):
            temp = temp.next

            if temp == self.head:
                print("Invalid position")
                return

        newnode.next = temp.next
        temp.next = newnode

    def display(self):
        temp = self.head

        if self.head is None:
            print("list is empty")
            return

        while True:
            print(f"{temp.data} -> ",end = " ")
        
            temp = temp.next

            if temp == self.head:
                break
        
        print("Head")
l1 = linkedlist()
l1.create_node()
print("list is\n")
l1.display()

l1.insert_at_first()
print("circular list is\n")
l1.display()

l1.insert_at_last()
print("circular list is\n")
l1.display()

l1.insert_at_position()
print("circular list is\n")
l1.display()
