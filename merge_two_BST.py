def mergeBST(root1, root2):
    st1 = []
    st2 = []
    pt1 = root1
    pt2 = root2
    b = True
    while pt1.left:
        st1.append(pt1)
        pt1 = pt1.left

    while pt2.left:
        st2.append(pt2.left)
        pt2 = pt2.left

    while b:


        if len(st1)==0 and len(st2)==0 and not pt1.left and not pt2.left:
            break
        if len(st1) == 0:
            while pt1.left:
                st1.append(pt1)
                pt1 = pt1.left
        if len(st2) == 0:
            while pt2.left:
                st2.append(pt2)
                pt2 = pt2.left
        if st1[len(st1)-1]>st2[len(st2)-1]:
            pt1 = st1.pop()
            print(pt1.data)
            pt1 = st1.pop()
            st1.append(pt1.right)
        else:
            pt2 = st2.pop()
            print(pt2.data)
            pt2 = st2.pop()
            st2.append(pt2.right)





class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        elif root.data == node.data:
            return
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
def traverseInorder(root):
    if root is not None:
        traverseInorder(root.left)
        print(root.data, end=" ")
        traverseInorder(root.right)
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,m = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        root1 = None
        for j in arr:
            if root1 is None:
                root1 = Node(j)
            else:
                insert(root1, Node(j))
        arr = list(map(int, input().strip().split()))
        root2 = None
        for j in arr:
            if root2 is None:
                root2 = Node(j)
            else:
                insert(root2, Node(j))
        mergeBST(root1, root2)
        print()
# Contributed by: Harshit Sidhwa

