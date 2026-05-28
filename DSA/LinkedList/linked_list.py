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

     #-------------------inserting at first------------------#           

    def insert_at_first(self): 
        data = int(input("enter data:\n"))

        newnode = node(data)

        newnode.next = self.head
        self.head = newnode
    
    #-------------------inserting at last------------------#


    def insert_at_last(self):
        data = int(input("enter data:\n"))
        newnode = node(data)

        temp = self.head

        while temp.next is not None:
            temp = temp.next
        temp.next = newnode

    #-------------------inserting at position------------------#
    def insert_at_position(self):
        data = int(input("enter data:\n"))
        pos = int(input("enter position:\n"))

        newnode = node(data)
        temp = self.head

        if pos == 0:    #edge case for inserting at first
            newnode.next = self.head
            self.head = newnode
            return


        for i in range(pos-1): #this move to previous  node
            temp = temp.next
        
        newnode.next = temp.next
        temp.next = newnode

#-------------------displaying linked list----------------#
    def display(self):
        temp = self.head

        while temp is not None:
            print(f"{temp.data} ->",end=" ")
            temp = temp.next
        print("None")


#object creation
l1 = linkedlist()
l1.create_node() #creating linked list

print("linked list: ")
l1.display() #displaying linked list

l1.insert_at_first() #inserting at first

print("linked list after inserting at first: ")
l1.display() #displaying linked list after inserting at first

l1.insert_at_last() #inserting at last
print("linked list after inserting at last: ")
l1.display() #displaying linked list after inserting at last

l1.insert_at_position() #inserting at position
print("linked list after inserting at position: ")
l1.display() #displaying linked list after inserting at position
