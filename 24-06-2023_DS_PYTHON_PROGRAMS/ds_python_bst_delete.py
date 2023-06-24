class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key,end=" ")
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    if key<node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node
def minvaluenode(node):
    current=node
    while(current.left is not None):
        current=current.left
    return current
def deletenode(root,key):
    if root is None:
        return root
    if key<root.key:
        root.left=deletenode(root.left,key)
    elif(key>root.key):
        root.right=deletenode(root.right,key)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        temp=minvaluenode(root.right)
        root.key=temp.key
        root.right=deletenode(root.right,temp.key)
    return root
root=None
root=insert(root,50)
root=insert(root,30)
root=insert(root,20)
root=insert(root,40)
root=insert(root,70)
root=insert(root,60)
root=insert(root,80)
print('inorder')
inorder(root)
print( '\ndelete 20')
root=deletenode(root,20)
print("inorder:modified tree")
inorder(root)
print("\ndelete 30")
root=deletenode(root,30)
print("inorder:modified tree")
inorder(root)














