import BT


def BFS(root):
  if root is None:
    return
  queue=[root]
  while queue:
    node=queue.pop(0)
    print(node.data,end=' ')
    if node.left is not None:
      queue.append(node.left)
    if node.right is not None:
      queue.append(node.right)

def DFS(root):
  if root is None:
    return
  print(root.data,end=' ')
  DFS(root.left)
  DFS(root.right)

def sequence(col,n):
  list=[]
  if col=="RED":
    for i in range(0,n):
      list.append(2*i+1)
  elif col=="GREEN":
    for i in range(0,n):
      list.append(2*(i+1))
  return list


col=input("Enter the colour(RED or GREEN):")
n=int(input("Enter the number of balls:"))
seq=sequence(col,n)
nodes=[None if ele is None else BT.Node(ele) for ele in seq]
print("The generated sequence is:")
for ele in seq:
  print(ele,end=" ")
print("\n")
root=BT.constructBT(nodes)
print("State space tree representation of the sequence (binary tree):\n")
BT.printBT(root)
print("\nBFS traversal:")
BFS(root)
print("\nDFS traversal:")
DFS(root)
print("\n")
