class Node:
   
   def __init__(self,initval,parent=None):
      self.val = initval
      self.left = None
      self.right = None
      self.parent = parent

   def put (self, val):
      self._put (val,self)	# call helper function

   def _put(self, val, current):

      if int(val) < int(current.val):
         # add to left subtree
         if current.left == None:
            current.left = Node(val,parent=current)
            print(val+" is new left child of "+current.val)
            dummy=input("")
         else:
            self._put(val,current.left)

      else:
         # add to right subtree
         if current.right == None:
            current.right = Node(val,parent=current)
            print(val+" is new right child of "+current.val)
            dummy=input("")
         else:
            self._put(val,current.right)


   def find_min(self):
       # Gets minimum node in a subtree

       current = self

       while current.left != None:
           current = current.left

       return current


   def replace_node_in_parent(self, pointer):
      # go to my parent & make it point at “pointer” instead of me
      if self.parent.left == self:
         self.parent.left = pointer
      else:
         self.parent.right = pointer
      if pointer != None:
         pointer.parent = self.parent


   def delete(self, item):

      if item < self.getRootData():
         self.left.delete(item)
      elif item > self.getRootData():
         self.right.delete(item)
      else:
         # delete this node

         if self.left != None and self.right != None:
            # both children are present
            successor = self.right.find_min()
            self.setRootData(successor.getRootData())
            successor.delete(successor.getRootData())

         elif self.left != None:
            # the node has only a left child
            self.replace_node_in_parent(self.left)

         elif self.left != None:
            # the node has only a right child
            self.replace_node_in_parent(self.right)

         else:
            # this node has no children
            self.replace_node_in_parent(None)

   def inOrder(self):
      if self.left == None:
         leftVal = ""
      else:
         leftVal = self.left.inOrder()+" "

      if self.right == None:
         rightVal = ""
      else:
         rightVal = " "+self.right.inOrder()

      return (leftVal+self.val+rightVal)

def main():

   myTree = Node("100")
   print("Root node is 100")
   myTree.put("50")
   myTree.put("150")
   myTree.put("25")
   myTree.put("125")
   myTree.put("140")
   myTree.put("110")
   myTree.put("145")
   myTree.put("75")
   myTree.put("130")
   myTree.put("175")

   print(myTree.inOrder())


main()
