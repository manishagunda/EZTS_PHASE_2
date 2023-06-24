class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class queue:
    def __init__(self):
        self.head=None
    
    def enqueue(self,data):#insert at begin
        if self.head is None:
            self.head = Node(data)
        else:
            ne=Node(data)
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=ne
            ne.next=None
            
    
    def dequeue(self):#delete at begin
        if self.head is None:
            print("queue is empty")
        else:
            temp=self.head
            self.head=temp.next
            temp.next=None
            print("deleted element is",temp.data)
            
    def display(self):
        if self.head is None:
            print("queue is empty")
        else:
            temp=self.head #temp=first node
            while temp:
                print(temp.data,end=' ') #temp.data means first node's data
                temp=temp.next
                
    def peek(self):
        if self.head is None:
            print("queue is empty")
        else:
            print("peek element",self.head.data)
        
            
obj=queue()
while(1):
    print("enter choice 1.enqueue 2.dequeue 3.display 4.peek 5.exit")
    choice=int(input())
    if choice==1:
        n=int(input("enter element"))
        obj.enqueue(n)
    elif choice==2:
        obj.dequeue()
    elif choice==3:
        obj.display()
    elif choice==4:
        obj.peek()
    elif choice==5:
        break
    else:
        print("enter correct choice")
        

        
        
