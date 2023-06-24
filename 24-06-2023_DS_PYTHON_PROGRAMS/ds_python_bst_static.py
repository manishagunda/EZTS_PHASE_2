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
    if root is None or root.val==k:
        return root
    if root.val<k:
        return search(root.right,k)
    return search(root.left,k)
r=Node(100)
r=insert(r,70)
r=insert(r,50)
r=insert(r,60)
r=insert(r,9)
r=insert(r,-3)
k=int(input("enter search ele"))
result=search(r,k)

if result is None:
    print("not found")
else:
    print("found")
