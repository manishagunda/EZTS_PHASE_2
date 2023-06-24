class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class linkedlist:
    def __init__(self):
        self.head=None
     #insert new node at the beginning   
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
        
    def detectandremoveloop(self):
        if self.head is None:#empty
            return
        if self.head.next is None:#one
            return
        slow_p=self.head
        fast_p=self.head
    
        while(slow_p and fast_p and fast_p.next):
            slow_p=slow_p.next
            fast_p=fast_p.next.next
            
            #if slow_p and fast_p meet at same point
            #there is a loop
            if slow_p==fast_p:
                print("meeting point", slow_p.data)
                slow_p=self.head
                #finding the beginning of loop
                while(slow_p.next != fast_p.next):
                    slow_p=slow_p.next
                    fast_p=fast_p.next
                    
                print("start of loop",fast_p.next.data)
                fast_p.next=None #remove loop
                
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next

llist=linkedlist()
llist.head=Node(50)
llist.head.next=Node(20)
llist.head.next.next=Node(15)
llist.head.next.next.next=Node(4)
llist.head.next.next.next.next=Node(10)

#create a loop for testing
extra=Node(1)
llist.head.next.next.next.next.next=extra
extra.next=llist.head.next

#llist.printlist()
llist.detectandremoveloop()
print("linked list after removing loop")
llist.printList()
                
            
            
            
            
            
            
            
            
            
            
            
            