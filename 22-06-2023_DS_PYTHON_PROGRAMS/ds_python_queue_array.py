queue=[]
def enqueue():
    e=int(input("enter element"))
    queue.append(e)
    print(queue)
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        a=queue.pop(0)
        print("popped element",a)
def peek():
    if not queue:
        print("queue is empty")
    else:
        print(queue[-1])
        
while(1):
    print("enter choice 1.enqueue 2.dequeue 3.peek 4.exit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        peek()
    elif choice==4:
        break
    else:
        print("enter correct choice")
        
    
    
        
    
    

