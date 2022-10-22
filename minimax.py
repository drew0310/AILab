from binarytree import build
import math

def buildtree(list):
  tree = build(list)
  return tree
  

def btree(limit):
  limit = limit + 1
  tree = [1]
  count = 0
  ele = 1  
  while(ele<2**limit-1):
    tree.append(tree[count]*2 + 1)
    tree.append(tree[count]*2 + 2)
    ele = ele + 2
    count = count + 1
  return tree
 
def minimax (curDepth, nodeIndex,
             maxTurn, tree,
             targetDepth):
 
   
    if (curDepth == targetDepth):
        return tree[nodeIndex]
     
    if (maxTurn):
        return max(minimax(curDepth + 1, nodeIndex * 2 + 1,
                    False, tree, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 2,
                    False, tree, targetDepth))
     
    else:
        return min(minimax(curDepth + 1, nodeIndex * 2 + 1,
                     True, tree, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 2,
                     True, tree, targetDepth))

if __name__ == "__main__":
  depth = int(input("Enter level: "))
  tree = btree(depth)
  Tree = build(tree)
  print(Tree)
  print("The optimal value is : ", end = "")
  print(minimax(0, 0, True, tree, depth))
  
