class BinaryTree:

   def __init__(self,initVal):
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











def preorder(tree):
   if tree != None:
      print(tree.getRootVal())
      preorder(tree.getLeftChild())
      preorder(tree.getRightChild())

def inorder(tree):
   if tree != None:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())

def postorder(tree):
   if tree != None:
      postorder(tree.getLeftChild())
      postorder(tree.getRightChild())
      print(tree.getRootVal())

def main():

   # create a sample tree

   myTree = BinaryTree(3)
   myTree.insertLeft(4)
   myTree.insertLeft(5)
   myTree.insertRight(6)
   myTree.insertRight(7)
   l = myTree.getLeftChild()
   r = myTree.getRightChild()
   l.insertRight(8)
   r.insertLeft(9)

   # print traversals
   print("inorder:")	# 4 5 8 3 9 7 6
   inorder(myTree)
   print("preorder:")	# 3 5 4 8 7 9 6
   preorder(myTree)
   print("postorder:")	# 4 8 5 9 6 7 3
   postorder(myTree)

main()
