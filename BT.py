import contextlib

  
class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None


def constructBT(nodes):
  for i in range(len(nodes)):
    node=nodes[i]
    if(node is not None):
      with contextlib.suppress(Exception):
        node.left=nodes[2*i+1]
      with contextlib.suppress(Exception):
        node.right=nodes[2*i+2]
  if nodes:
    return nodes[0]
  else:
    return None

def printBT(root,level=0):
  if root is None:
    return
  printBT(root.right,level+1)
  print('  '*level,root.data)
  printBT(root.left,level+1)
