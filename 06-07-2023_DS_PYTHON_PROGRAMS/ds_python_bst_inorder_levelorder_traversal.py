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
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def level_order(root):
    queue=[root]
    print("level order traversal")
    while len(queue)!=0:
        ele=queue.pop(0)
        if ele.left!=None:
            queue.append(ele.left)
        if ele.right!=None:
            queue.append(ele.right)
        print(ele.val)
r=Node(50)
r=insert(r,30)
r=insert(r,20)
r=insert(r,40)
r=insert(r,70)
r=insert(r,60)
r=insert(r,80)
inorder(r)
level_order(r)

    
        

    
