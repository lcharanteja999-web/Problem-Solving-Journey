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
      
#----------------------------------search function-----------------------------------
    def search(self,key):

        temp = self.head

        if self.head is None:
            return

        if self.head is None:
            return
        
        while temp is  not None:
        
            if temp.data == key:
                return True
            
            temp = temp.next
        
        return False
    
l1 = DoublyLinkedlist()
l1.create_node()

key = int(input("enter data to search "))
if l1.search(key):
    print("Element found")
else:
    print("Element not found")
        
        

