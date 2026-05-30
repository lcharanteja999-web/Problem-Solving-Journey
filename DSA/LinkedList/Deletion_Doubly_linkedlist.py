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

    #-------------------------deleting at first---------------------
    def delete_at_first(self):
        temp = self.head

        if self.head is None:
            print("list is empty\n")
            return

        if self.head.next is None:
            self.head = None
            return


        self.head = self.head.next
        self.head.prev = None

    #-------------------------deletion at last------------------------------

    def delete_at_last(self):
        temp = self.head

        if self.head is None:
            print("list is empty\n")
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        while temp.next is not None:
            temp = temp.next

        temp.prev.next = None

    #--------------------------delete at position------------------

    def delete_at_position(self):
        temp = self.head

        pos = int(input("enter position\n"))

        if pos <= 0:
            print("invalid position\n")
            return

        if self.head is None:
            print("list is empty\n")
            return

        #edge casse for delete first node
        if pos == 1:
            self.head = self.head.next

            if self.head is not None:
                self.head.prev = None

            return

        for _ in range(1, pos):
            temp2 = temp
            temp = temp.next

        # edge case for delete last node
        if temp.next is None:
            temp2.next = None
            temp.prev = None
            temp = None
            return

        # edge case for delete middle node
        temp2.next = temp.next
        temp.next.prev = temp2

        temp = None

#---------------------------display function-----------------

    def forward_display(self):

        temp = self.head

        while temp is not None:
            print(f"{temp.data} <-> ",end = " ")   #forward traversal
            temp = temp.next
        print("Null\n")

   
l1 = DoublyLinkedlist()  #creating objects
l1.create_node()       
l1.forward_display()

l1.delete_at_first()          #delete at first
l1.forward_display()

l1.delete_at_last()  #delete at last
l1.forward_display()

l1.delete_at_position() #delete at position
l1.forward_display()


