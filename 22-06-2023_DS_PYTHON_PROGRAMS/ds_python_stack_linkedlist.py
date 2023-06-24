class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.head=None
    
    def push(self,data):#insert at begin
        if self.head is None:
            self.head = Node(data)
        else:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
    
    def pop(self):#delete at begin
        if self.head is None:
            print("stack is empty")
        else:
            temp=self.head
            self.head=temp.next
            temp.next=None
            print("popped deleted is",temp.data)
            
    def display(self):
        if self.head is None:
            print("stack is empty")
        else:
            temp=self.head #temp=first node
            while temp:
                if temp.next is not None:
                    print(temp.data,end=' ') #temp.data means first node's data
                temp=temp.next
                
    def peek(self):
        if self.head is None:
            print("stack is empty")
        else:
            print("peek element",self.head.data)
        
            
obj=stack()
while(1):
    print("enter choice 1.push 2.pop 3.display 4.peek 5.exit")
    choice=int(input())
    if choice==1:
        n=int(input("enter element"))
        obj.push(n)
    elif choice==2:
        obj.pop()
    elif choice==3:
        obj.display()
    elif choice==4:
        obj.peek()
    elif choice==5:
        break
    else:
        print("enter correct choice")
        

        
        