# stack and queue

import array

class Node:
    def __init__(self,value):
        self.next = None
        self.value = value

# push function to stack
def push(stackTop, value):
    tempNode = Node(value)
    tempNode.next = stackTop
    return tempNode


def pop(stackTop):
    tempVal = stackTop.value
    tempNode = stackTop
    stackTop = stackTop.next
    del(tempNode)
    return tempVal, stackTop
    
def traverseStack(stackTop):
    tempNode = stackTop
    print ("print stack top to bottom")
    while(tempNode != None):
        print (tempNode.value)
        tempNode = tempNode.next


def findMinimum(stackTop):
    return None
    
def findMaximum(stackTop):
    return None

#create root Node
stackTop = None

#push value to stack
stackTop = push(stackTop, 1)
stackTop = push(stackTop, 2)
stackTop = push(stackTop, 3)
stackTop = push(stackTop, 4)
traverseStack(stackTop)
val, stackTop = pop(stackTop)
print ('pop ', val)
traverseStack(stackTop)
stackTop = push(stackTop, 5)
traverseStack(stackTop)

