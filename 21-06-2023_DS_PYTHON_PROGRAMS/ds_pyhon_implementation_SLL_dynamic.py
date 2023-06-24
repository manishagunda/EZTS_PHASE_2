class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class linkedlist:
    def __init__(self):
        self.head=None
        self.last_node=None
        
    def append(self,data):
        if self.last_node is None:
            self.head=Node(data)
            self.last_node=self.head
        else:
            self.last_node.next=Node(data)
            self.last_node=self.last_node.next
            
    def insert_beginning(self,data):
        nb=Node(a)
        nb.next=self.head
        self.head=nb
    
    def insert_end(self,b):
        ne=Node(b)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
        ne.next=None
        
    def insert_pos(self,pos,c):
        np=Node(c)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
            
        np.next=temp.next
        temp.next=np
        
    def delete_begin(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        
    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None #last but before node
        
    def delete_pos(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(0,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
        
    def search(self,num):
        flag=0
        temp=self.head
        while temp:
            if temp.data==num:
                flag=1
                break
            temp=temp.next
        if flag==1:
            print("yes,found")
        else:
            print("not found")
        
    def display(self):
        current=self.head
        while current is not None:
            print(current.data, end=" ")
            current=current.next
            
a_llist=linkedlist()
n=int(input("enter num of elements"))
for i in range(n):
    data=int(input("enter elements"))
    a_llist.append(data)
    
print("the linked list: ",end=" ")
a_llist.display()

print(" ")
a=int(input("enter num to insert at begin"))
print("after inserting at begin")
a_llist.insert_beginning(a)
a_llist.display()

print(" ")
b=int(input("enter num to insert at end"))
print("after inserting at end")
a_llist.insert_end(b)
a_llist.display()

print(" ")
pos=int(input("enter position"))
c=int(input("enter num to insert at pos"))
print("after inserting at position")
a_llist.insert_pos(pos,c)
a_llist.display()

print(" ")
print("after deleting at begin")
a_llist.delete_begin()
a_llist.display()
print(" ")
print("after deleting at end")
a_llist.delete_end()
a_llist.display()
print(" ")
pos=int(input("enter position"))
print("after deleting at pos")
a_llist.delete_pos(pos)
a_llist.display()

print(" ")
num=int(input("enter number"))
a_llist.search(num)


