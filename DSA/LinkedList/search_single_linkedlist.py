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
                
#---------------------search function----------------------------
    def search(self,key):

        temp = self.head

        if self.head is None:
            return

        while temp is not None:
            if temp.data == key:
                return True
            
            temp = temp.next
        
        return False
        
      

l1 = linkedlist()
l1.create_node()

key = int(input("enter element to search\n"))
if l1.search(key):
    print("element found")
else:
    print("element not found")

        
