# construct a binary tree with minimal height given a sorted array 

import array

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

def addToTree(arr, start, end):

    if(end < start):
        #print ("end is less than start")
        return None
        
    #print ("The sorted array in this addToTree call is : ")
    #for i in range (start, end):
    #    print (arr[i])

    mid = (start+end)/2
    root = Node(arr[mid])
    #print("mid",mid) 
    print "insert array mid to tree ", arr[mid]
    root.left = addToTree(arr, start, mid-1)
    root.right = addToTree(arr, mid+1, end)
    return root

def MinimalHeightfromSortedArray():
    #Given a sorted array 
    arr= array.array('i',[0, 1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15]) 
    #create a binary tree with minimal height 
    #solution:
    # 1. find middle of the array and make that element as the root of BST 
    #2. Construct the BST in-order with the root in #1 
    print "length of given array and middle index, value"
    print len(arr), len(arr)/2, arr[(len(arr)/2)]
    
    return addToTree(arr, 0, len(arr)-1)
    
    
#create root Node

rootBST = MinimalHeightfromSortedArray()
print "in-order traversal"
printInorder(rootBST)

#print "preorder traversal"
#printPreorder(rootBST)

#print "postorder traversal"
#printPostorder(rootBST)

height = maxDepth(rootBST)
print ""
print "height of the minimal height tree is", height

#checking if the tree is balanced
balance = isBalanced(rootBST)
if (balance is True):
    print "The tree is balanced"
else:
    print "The tree is NOT balanced"
