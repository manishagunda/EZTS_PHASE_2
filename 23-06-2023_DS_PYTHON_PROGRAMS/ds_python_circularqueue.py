class cq():
    def __init__(self,size):
        self.size=size
        
        self.queue=[None for i in range(size)]
        self.front=self.rear=-1
    
    def enqueue(self,data):
        if((self.rear+1) % self.size==self.front):
            print("queue is full")
        elif(self.front==-1):
            self.front=0
            self.rear=0
            self.queue[self.rear]=data
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=data
    def dequeue(self):
        if(self.front==-1):
            print("queue is empty")
        elif(self.front ==self.rear):
            temp=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return temp
    def display(self):
        if(self.front==-1):
            print("queue is empty")
        elif(self.rear>= self.front):
            print("elements in circular queue",end=" ")
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=" ")
                print()
        else:
            print("elements in circular queue",end=" ")
            for i in range(self.front,self.size):
                print(self.queue[i],end=" ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end=" ")
            print()
        if((self.rear+1) % self.size==self.front):
            print("queue is full")
o=cq(6)
o.enqueue(14)
o.enqueue(22)
o.enqueue(13)
o.enqueue(-6)
o.display()
print("del element= ",o.dequeue())
print("del element= ",o.dequeue())
o.display()
o.enqueue(9)
o.enqueue(20)
o.enqueue(5)
o.display()
o.enqueue(100)
o.display()


