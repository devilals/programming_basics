
# A Python class that represents an individual node 
# in a Binary Tree
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

# A function to do inorder tree traversal
def printInorder(root):
 
    if root:
 
        # First recur on left child
        printInorder(root.left)
 
        # then print the data of node
        print(root.val),
 
        # now recur on right child
        printInorder(root.right)
 

# A function to do postorder tree traversal
def printPostorder(root):
 
    if root:
 
        # First recur on left child
        printPostorder(root.left)
 
        # the recur on right child
        printPostorder(root.right)
 
        # now print the data of node
        print(root.val),
 
 
# A function to do postorder tree traversal
def printPreorder(root):
 
    if root:
 
        # First print the data of node
        print(root.val),
 
        # Then recur on left child
        printPreorder(root.left)
 
        # Finally recur on right child
        printPreorder(root.right)
        

# Compute the "maxDepth" of a tree -- the number of nodes 
# along the longest path from the root node down to the 
# farthest leaf node
def maxDepth(node):
    if node is None:
        return 0 ; 
 
    else :
 
        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
 
        # Use the larger one
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1
         

def isBalanced(node):
    #left sub tree is balanced?
    #right subtree is balanced? 
    # the difference between the height of left subtree and right subtree is not more than 1
    
    if node is None:
        return True
    lheight = maxDepth(node.left)
    rheight = maxDepth(node.right)
        
    if ((isBalanced(node.left)) and (isBalanced(node.right)) and (abs(lheight-rheight) <=1)):
        return True
        
    return False        

#create root Node
# Driver code
root = Node(1)
root.left      = Node(2)
root.right     = Node(3)
root.left.left  = Node(4)
root.left.right  = Node(5)
root.left.right.right  = Node(6)
root.right.left  = Node(7)
root.left.right.right.left  = Node(8)
#print "Preorder traversal of binary tree is"
#printPreorder(root)
 
#print "\nInorder traversal of binary tree is"
#printInorder(root)
 
#print "\nPostorder traversal of binary tree is"
#printPostorder(root)
height = maxDepth(root)
print "height of the tree is", height

balance = isBalanced(root)
if (balance is True):
    print "The tree is balanced"
else:
    print "The tree is NOT balanced"
    
    
    
