class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
    
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        nb.previous=None
        self.head=nb
    
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
        ne.previous=temp
        ne.next=None
        
    def insert_pos(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(0,pos-1):
            temp=temp.next
            
        np.next=temp.next
        temp.previous=np
        temp.next=np
        temp.next.previous=np
        
    def delete_begin(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.head.previous=None
    
    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
        
    def delete_pos(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(0,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
        temp.previous=prev
            
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head #temp=first node
            while temp:
                if temp.next is not None:
                    print(temp.data,"<->",end=' ')
                else:
                    print(temp.data,end=' ') #temp.data means first node's data
                temp=temp.next
obj=DLL()
#node creation_initialising
n=Node(10)#so n.data in Node class will be 10
obj.head=n   #assigning first node as head
n1=Node(20)
n.next=n1#next node value
n.previous=None
n2=Node(30)
n1.next=n2
n1.previous=n
n3=Node(40)
n2.next=n3
n2.previous=n1
n4=Node(50)
n3.next=n4
n3.previous=n2
n5=Node(60)
n4.next=n5
n4.previous=n3
obj.display()
print(" ")
print("after inserting 555 at bagin")
obj.insert_beginning(555)
obj.display()
print(" ")
print("after inserting 90 at end")
obj.insert_end(90)
obj.display()
print(" ")
print("after inserting 70 at pos 3")
obj.insert_pos(3,70)
obj.display()
print(" ")
print("after deleting at begin")
obj.delete_begin()
obj.display()
print(" ")
print("after deleting at end")
obj.delete_end()
obj.display()
print(" ")
print("after deleting at pos")
obj.delete_pos(2)
obj.display()
'''print(" ")
num=int(input("enter number"))
obj.search(num)'''

