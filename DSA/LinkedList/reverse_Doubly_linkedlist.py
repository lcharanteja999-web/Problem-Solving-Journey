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

    #---------------------------------------reverse function-------------------------------------
    
    def reverse(self):
        temp = None
        current = self.head
        
        while current:
            #swap prev and next

            temp = current.prev
            current.prev = current.next
            current.next = temp
        
        current = current.prev  #move to next node

        if temp:
            self.head = temp.prev          #  Set head to the original last node (new head after reversal)
            return

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
