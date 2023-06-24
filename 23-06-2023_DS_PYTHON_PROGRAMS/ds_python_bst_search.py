class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val==key:
            return root
        elif root.val<key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root
def search(root,k):
    f=0
    if root is None or root.val==k:
        f=1
    if root.val<k:
        return search(root.right,k)
    return search(root.left,k)
    if f==1:
        print("found")
    else:
        print("not found")
r=Node(100)
r=insert(r,70)
r=insert(r,50)
r=insert(r,60)
r=insert(r,9)
r=insert(r,-3)
k=int(input("enter search ele"))
search(r,k)
