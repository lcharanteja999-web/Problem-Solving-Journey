MAX = 5

class stack:   #creating a class named stack
    def __init__(self,size):
        self.size = size
        self.stack = [None] * size  #creating a list of size 'size' and initializing all elements to None
        self.top = -1  #initializing top to -1, indicating an empty stack

    #-----------------------push operation-------------------------
    
    def push(self,data):
        if self.top == MAX -1:
            print("Stack overflow") #checking if stack is full
            return
        
        self.top += 1 #incrementing top by 1
        self.stack[self.top] = data #adding data to the top of the stack
        print(f"{data} pushed successfully") 
    
    #-----------------------------pop operation----------------------

    def pop(self):
        if self.top == -1:
            print("stack underflow")  #checking if stack is empty
            return
        data = self.stack[self.top]
        self.top -= 1
        return data
    
    #----------------------------peek operation--------------------------

    def peek(self):
        if self.top == -1:
            print("stack is empty") #checking if stack is empty
            return  
        
        return self.stack[self.top] #returning the top element of the stack
    
    #-----------------------------empty operation-----------------------

    def is_empty(self):
        if self.top == -1:
            print("Stack is empty")
            
        else:
            print("stack is not empty")

    #---------------------------is full operation-----------------------

    def is_full(self):
        if self.top == MAX -1:
            print("stack is full")

        else:
            print("stack is not full")
    
    #-----------------------------count operation-------------------------

    def count(self):
        return self.top + 1 #returning the number of elements in the stack
    
    def display(self):
        if self.top == -1:
            print("stack is empty")
            return
        print("stack elements are : ", end = " ")

        for i in range(self.top, -1, -1):
            print(self.stack[i],end = " ")

s = stack(MAX) #creating an object of stack class with size MAX

while True:
    print("\n------------------STACK MENU--------------------")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Is Empty")
    print("5. Is Full")
    print("6. Count")
    print("7. Display")
    print("8. Exit")

    choice = int(input("Enter your choice : ")) 

    if choice == 1:
        data = int(input("Enter data to push : "))
        s.push(data)

    elif choice == 2:

        print(f"Popped element is : {s.pop()}")

    elif choice == 3:

        print(f"Top element is : {s.peek()}")

    elif choice == 4:

        s.is_empty()

    elif choice == 5:

        s.is_full()

    elif choice == 6:

        print(f"Number of elements in stack : {s.count()}")

    elif choice == 7:

        s.display()

    elif choice == 8:
        break

    else:
        print("Invalid choice")
