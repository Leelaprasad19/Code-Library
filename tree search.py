class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def search(root,key):
     
    if root is None or root.val == key:
        return root
        
    if root.val < key:
        return search(root.right,key)
    return search(root.left,key)
 
# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.val,end=' ')
#         inorder(root.right)
        
# def preorder(root):
#     if root:
#         print(root.val,end=' ')
#         preorder(root.left)
#         preorder(root.right)

# def postorder(root):
#     if root:
#         postorder(root.left)
#         postorder(root.right)
#         print(root.val,end=' ')
 
n = int(input())
key = int(input())

a = list(map(int, input().split()))

root = None
for i in a:
    root = insert(root,i)
 
# preorder(root)
# print()
# inorder(root)
# print()
# postorder(root)
# print()

if(search(root, key)):
    print("Key found")
else:
    print("Key not found")