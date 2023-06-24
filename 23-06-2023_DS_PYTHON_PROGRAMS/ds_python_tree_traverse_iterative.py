class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
def inorder(root):
    current=root
    stack=[]
    while True:
        if current is not None:
            stack.append(current)
            current=current.left
        elif(stack):
            current=stack.pop()
            print(current.data,end=" ")
            current=current.right
        else:
            break
    print()
root=Node(100)
root.left=Node(400)
root.right=Node(500)
root.left.left=Node(700)
root.left.right=Node(600)
root.right.left=Node(800)
root.right.right=Node(200)
root.left.right.left=Node(900)
root.right.right.left=Node(300)
inorder(root)
    