class node:
    def __init__(self,data,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedlist:
    def __init__(self):
        self.head = None

#-----------------------------create node function---------------------------
    
    def create_node(self):

        temp = self.head

        while True:
            choice = int(input("enter 1 to create node 0 to stop: "))

            if choice == 0:
                break
                
            data = int(input("enter data "))
            newnode = node(data)

            if self.head is None: #first node
                self.head = newnode
                temp = newnode
            else:
                temp.next = newnode
                newnode.prev = temp
                temp = temp.next

        if self.head is not None:
            temp.next = self.head
            self.head.prev = temp

#-------------------------------------insert at first-----------------------------

    def insert_at_first(self):
        data = int(input("enter data "))
        newnode = node(data)

        if self.head is None:  #edge case if head is none
            self.head = newnode
            newnode.next = newnode
            newnode.prev = newnode
            return

        temp = self.head

        while temp.next != self.head:
            temp = temp.next    

        newnode.next = self.head
        newnode.prev = temp

        temp.next = newnode
        self.head.prev = newnode

        self.head = newnode

#-----------------------------------insert at last--------------------------
    
    def insert_at_last(self):
        data = int(input("enter data "))
        newnode = node(data)

        # Empty list
        if self.head is None:
            self.head = newnode
            newnode.next = newnode
            newnode.prev = newnode
            return

        temp = self.head

        # Move to last node
        while temp.next != self.head:
            temp = temp.next

        # Connect new node
        newnode.next = self.head
        newnode.prev = temp

        temp.next = newnode
        self.head.prev = newnode


    #---------------------------insert at position--------------------------
    def insert_at_position(self):

        temp = self.head

        data = int(input("enter data "))
        newnode = node(data)
        pos = int(input("enter position "))

        if pos <= 0:
            print("invalid position")
            return

        if self.head is None:
            self.head = newnode
            newnode.next = newnode
            newnode.prev = newnode
            return

        if pos == 1:

            while temp.next != self.head:
                temp = temp.next

            newnode.next = self.head
            newnode.prev = temp

            temp.next = newnode
            self.head.prev = newnode

            self.head = newnode
            return

        for i in range(1, pos - 1):
            temp = temp.next

        newnode.next = temp.next
        newnode.prev = temp

        temp.next.prev = newnode
        temp.next = newnode


    def forward_display(self):

        temp = self.head

        if self.head is None:
            print("List is empty")
            return

        while True:
            print(f"{temp.data} <-> ", end=" ")

            temp = temp.next

            if temp == self.head:
                break

        print("HEAD")

    def backward_display(self):

        if self.head is None:
            print("List is empty")
            return

        temp = self.head.prev

        while True:
            print(f"{temp.data} <-> ", end=" ")

            temp = temp.prev

            if temp == self.head.prev:
                break

        print("TAIL")

l1 = DoublyLinkedlist()

l1.create_node()

print("forward Display ")
l1.forward_display()

print("backward Display ")
l1.backward_display()

l1.insert_at_first()
print("after insert at first:")
l1.forward_display()

l1.insert_at_last()
print("after insert at last:")
l1.forward_display()

l1.insert_at_position()
print("after insert at position:")
l1.forward_display()
