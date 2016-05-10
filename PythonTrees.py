def binaryTree(initdata):
   return [ initdata, [], [] ]

def getRootVal(root):
   return root[0]

def setRootVal(root, newVal):
   root[0] = newVal

def getLeftChild(root):
   return root[1]

def getRightChild(root):
   return root[2]

def insertLeft(root,newBranch):
   t = root.pop(1)
   if len(t) > 1:                        # if something already
      root.insert(1,[newBranch,t,[] ] )  # there, push it down as
   else:                                 # the new left child
      root.insert(1,[newBranch,[],[] ] )

def insertRight(root,newBranch):
   t = root.pop(2)
   if len(t) > 1:                        # if something already
      root.insert(2,[newBranch,[],t ] )  # there, push it down as
   else:                                 # the new right child
      root.insert(2,[newBranch,[],[] ] )

def main():

    print ("Tree functions loaded.")
    while True:
        inString = input(">>> ")
        eval (inString)

main()
