


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
##Structure of node
'''
class Node:
    data=0
    left=None
    right=None
'''
##Complete this function
def getCountOfNode(root,l,h):
    if root == None:
        return 0
    if root.data in range(l,h+1):
        return getCountOfNode(root.left,l,root.data)+getCountOfNode(root.right,root.data, l)+1
    elif root.data > l:
        return getCountOfNode(root.left,l,root.data)
    elif root.data < h:
        return getCountOfNode(root.right,root.data, l)