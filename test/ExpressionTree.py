#  File: ExpressionTree.py
#  Description: We want a driver that will sort various lists using algorithms, calculating their execution time, and printing a table of results: Bubble Sort, Insertion Sort, Selection Sort, Shell Sort, Merge Sort, and Quick Sort
#  Student's Name: Minh-Tri Ho
#  Student's UT EID: mh47723
#  Course Name: CS 313E
#  Unique Number: 50940
#
#  Date Created: 04/29/16
#  Date Last Modified: 04/29/16

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

class Queue(object):
  def __init__(self):
    self.queue = []

  def enqueue(self,item):
    self.queue.append(item)

  def dequeue(self):
    return (self.queue.pop(0))

  def isEmpty(self):
    return (len(self.queue) == 0)

  def size(self):
    return (len(self.queue))

class Node(object):
    def __init__(self,initdata = None):
        self.data = initdata
        self.left = None            # always do this – saves a lot
        self.right = None           # of headaches later!

    def getData (self):
        return self.data            # returns a POINTER

    def setData (self, newData):
        self.data = newData         # changes a POINTER

#Using LinkedList with Sentinel
class LinkedList (object):
    def __init__(self):
        header = Node(None)
        self.head = header

    def getLast(self):
        if self.head.getNext() != None:
            current = self.head.getNext()

            while current.getNext() != None:
                current = current.getNext()
        else:
            current = self.head
        return current

    def getLength (self):
        # Return the number of items in the list
        current = self.head.getNext()
        count = 0

        while current != None:
            count += 1
            current = current.getNext()

        return count

    def addFirst (self, item):
        # Add an item to the beginning of the list
        temp = Node(item)
        temp.setNext(self.head.getNext())
        self.head.setNext(temp)

    def addLast (self, item):
        # Add an item to the end of a list
        newLast = Node(item)
        current = self.getLast()
        current.setNext(newLast)

    def addInOrder (self, item):
        # Insert an item into the proper place of an ordered list.
        # This assumes that the original list is already properly
        #    ordered.
        current = self.head.getNext()
        previous = self.head
        stop = False

        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        temp.setNext(current)
        previous.setNext(temp)

    def addInReverseOrder (self, item):
        # Insert an item into the proper place of an ordered list in reverse order.
        # This assumes that the original list is already properly
        #    ordered.
        current = self.head.getNext()
        previous = self.head
        stop = False

        while current != None and not stop:
            if current.getData() < item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        temp.setNext(current)
        previous.setNext(temp)

    def findUnordered (self, item):
        # Search in an unordered list
        #    Return True if the item is in the list, False
        #    otherwise.
        current = self.head.getNext()
        found = False

        while current != None and not found:
            #We find the item
            if current.getData() == item:
                found = True
            #Otherwise we go to the next one
            else:
                current = current.getNext()

        return found

    def findOrdered (self, item):
         # Search in an ordered list
         #    Return True if the item is in the list, False
         #    otherwise.
         # This method MUST take advantage of the fact that the
         #    list is ordered to return quicker if the item is not
         #    in the list.
         current = self.head.getNext()
         found = False
         stop = False
         while current != None and not found and not stop:
            #We find the item
            if current.getData() == item:
                found = True
            #Otherwise we continue
            else:
                #if we didn't get pass the a value that would be above it
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

         return found

    def delete (self, item):
        # Delete an item from an unordered list
        #    if found, remove the item from the list and
        #    return True; otherwise, return False.

        current = self.head.getNext()
        previous = self.head
        found = False

        while current != None and not found:
            #If we find it, we set the next one as the next one of the last one, skipping the one to delete
            if current.getData() == item:
                found = True
                previous.setNext(current.getNext())
            else:
                previous = current
                current = current.getNext()

        return found

    def __str__ (self):
        # Return a string representation of data suitable for printing.
        #    Long lists (more than 10 elements long) should be neatly
        #    printed with 10 elements to a line, two spaces between
        #    elements
        res = ""
        current = self.head.getNext()
        for i in range(1,self.getLength()+1):
            #DEBUG: print(str(current.getData()))
            #We add the current data to the result
            res += str(current.getData())

            #If we get to the tenth element, we go to the next line
            if(i%10 == 0):
                res += "\n"
            #Otherwise we add a separator
            else:
                if i != self.getLength():
                    res  += " - "
            current = current.getNext()
        return res

    def copyList (self):
         # Return a new linked list that's a copy of the original,
         #    made up of copies of the original elements.  Do not
         #    change the original list.
         res = LinkedList()
         current = self.head.getNext()
         for i in range(1, self.getLength()+1):
             #We add the data to the new list, added at the end
             res.addLast(current.getData())
             current = current.getNext()
         return res

    def sortList (self,direction):
        # Take a linked list and return the same list with elements
        #    sorted.  If direction is "I", then the list should
        #    be sorted in increasing order;  if direction is "D",
        #    then it should be decreasing order.
        # Do NOT use a sort function:  do this by iteratively
        #    traversing the list, removing elements, and then
        #    inserting each item into the correct place in the
        #    updated list.
        temp = self.copyList()
        self.head = Node(None)
        current = temp.head.getNext()
        if direction == "I":
            for i in range(temp.getLength()):
                self.addInOrder(current.getData())
                current = current.getNext()
        elif(direction == "D"):
            for j in range(temp.getLength()):
                self.addInReverseOrder(current.getData())
                current = current.getNext()

    def isSorted (self):
        # Return True if a list is sorted in ascending (alphabetical)
        #    order, or False otherwise
        current = self.head.getNext()
        previous = self.head

        #If there is only one element, it's automatically sorted
        if(self.getLength() == 1):
            return True
        #Otherwise
        else:
            previous = current
            current = current.getNext()
            #We check if the current one is higher that the previous one
            while current != None:
                #Otherwise we return False
                if current.getData() < previous.getData():
                    return False
                previous = current
                current = current.getNext()

        return True

    def isEmpty (self):
        # Return True if a list is empty, or False otherwise
        return self.head.getNext() == None

    def mergeList (self, b):
        # Return a new ordered list whose elements consist of the
        #    elements of two ordered lists combined.  The original
        #    two lists should not be changed.
        res = LinkedList()

        #Add elements of List self
        current = self.head.getNext()
        while current != None:
            res.addInOrder(current.getData())
            current = current.getNext()

        #Add elements of List b
        current = b.head.getNext()
        while current != None:
            res.addInOrder(current.getData())
            current = current.getNext()

        #Returns the result
        return res

    def compareList (self,b):
        # Given two lists, return a new ordered list whose elements
        #    consist of items that appear in both of the two given
        #    lists.  The original two lists should not be changed.
        res = LinkedList()
        current = self.head.getNext()
        while current != None:
            #If we find the element of list b in the first list, we add it
            if b.findUnordered(current.getData()):
                res.addInOrder(current.getData())
            current = current.getNext()
        return res

    def isEqual (self, b):
        # Test if two lists are equal, item by item, and return True.
        res = True
        current = self.head.getNext()
        current2 = self.head.getNext()

        #If they are not the same length, they cannot be the same
        if(self.getLength() != b.getLength()):
            return False

        #Otherwise we compare element by element
        while current != None:
            if(current != current2):
                res = False
            current = current.getNext()
            current2 = current2.getNext()

        return res

    def removeDuplicates (self):
        # Modify a list, keeping only the first occurrence of an element
        #    and removing all duplicates.  Do not change the order of
        #    the remaining elements.
        res = LinkedList()
        current = self.head.getNext()
        while current != None:
            #If the element doesn't already exist in our new list, we add it
            if res.findUnordered(current.getData()) == False:
                res.addLast(current.getData())
            current = current.getNext()

        return res

class BinaryTree:
    def __init__(self,initVal = None):
        self.data = initVal
        self.left = None
        self.right = None

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setRootVal(self,value):
        self.data = value

    def getRootVal(self):
        return self.data

    def __str__(self):
        return self.data

    # Prints out all nodes at the given level
    def printLevel (self, level):
        #init current node, queue, string, position, starting and ending
        # positions of nodes at level x
        cur = self
        q = Queue()
        st = ''
        pos = 1
        start = 1
        for i in range(level-1):
          start += 2**(i)
        end = start + 2**(level-1) - 1

        #go through the tree
        q.enqueue(cur)
        while(pos <= end):
          if(not q.isEmpty()):
            cur = (q.dequeue())
            if(pos >= start and cur != None):
              print(cur.data)
              st += str(cur.data)+ ' '
            if(cur != None):
              q.enqueue(cur.left)
              q.enqueue(cur.right)
          pos += 1

        # return string with all the nodes.data
        return st

    def createTree (self, expr):
        #Operators are members of the set ['+', '-', '*', '/']. No other operators will be used in this homework assignment. Operators are stored in the tree's internal nodes.
        operators = "+-*/"

        st = Stack()
        for i in range(len(expr)):
            token = expr[i]
            if(token == "("):
                self.left = BinaryTree()
                st.push(self)
                self = self.left
            elif(token == ")"):
                if(not(st.isEmpty())):
                    self = st.pop()
            elif(token in operators):
                self.setRootVal(token)
                st.push(self)
                self.right = BinaryTree()
                self = self.right
            else:
                self.setRootVal(token)
                self = st.pop()

    def evaluate (self):
        operators = "+-*/"
        if(self.getRootVal() == None):
            return 0
        elif(not(self.getRootVal() in operators)):
            return float(self.getRootVal())
        else:
            if(self.getRootVal() == "+"):
                return(self.getLeftChild().evaluate() + self.getRightChild().evaluate())
            elif(self.getRootVal() == "-"):
                return(self.getLeftChild().evaluate() - self.getRightChild().evaluate())
            elif(self.getRootVal() == "*"):
                return(self.getLeftChild().evaluate() * self.getRightChild().evaluate())
            elif(self.getRootVal() == "/"):
                return(self.getLeftChild().evaluate() / self.getRightChild().evaluate())

    def preOrder(self):
        print(self.data, end = " ")
        if(self.left != None):
            self.getLeftChild().preOrder()
        if(self.right != None):
            self.getRightChild().preOrder()

    def postOrder (self):
        if(self.left != None):
            self.getLeftChild().postOrder()
        if(self.right != None):
            self.getRightChild().postOrder()
        print(self.data, end = " ")

def main():
    #Initialization

    #Operands will be either integers or floating point numbers. Operands are stored in the tree's leaf nodes.
    #You must use a linked list implementation for your expression tree.
    #You must use a stack to evaluate the expression tree.

    #Store the expression in a tree structure.
    file = open('./treedata.txt', 'r')
    expression = []
    exprNb = 0
    exprLi = [] #list of Stack containing the expressions
    for line in file:
        #Store the expressions
        exprNb += 1
        exprLi.append(line.split())

        print("Infix expression: " + line)
        expr = line.split()
        bin = BinaryTree()
        bin.createTree(expr)
        res = bin.evaluate()
        print("  Value: " + str(res))
        print("  Prefix expression: ", end = " ")
        bin.preOrder()
        print("\n  Postfix expression: ", end = " ")
        bin.postOrder()
        print("\n")

main()
