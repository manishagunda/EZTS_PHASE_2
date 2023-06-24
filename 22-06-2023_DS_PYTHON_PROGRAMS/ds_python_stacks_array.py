stack=[]
def push():
    e=int(input("enter element"))
    stack.append(e)
    print(stack)
def pop():
    if not stack:
        print("stack is empty")
    else:
        a=stack.pop()
        print("popped element",a)
def show():
    if not stack:
        print("stack is empty")
    else:
        print(stack)
        
def evenodd():
    stack1=[]
    stack2=[]
    if not stack:
        print("stack is empty")
    else:
        n=len(stack)
        for i in range(0,n):
            if(stack[i]%2==0):
                stack1.append(stack[i])
            else:
                stack2.append(stack[i])
    print("even stack",stack1)
    print("odd stack",stack2)
                
def peek():
    if not stack:
        print("stack is empty")
    else:
        print(stack[-1])
        
while(1):
    print("enter choice 1.push 2.pop 3.show 4.evenodd 5.peek 6.exit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        show()
    elif choice==4:
        evenodd()
    elif choice==5:
        peek()
    elif choice==6:
        break
    else:
        print("enter correct choice")
        
    
    
        
    
    
