import random
import BT

res=[]

def DLSUtil(root,limit):
  if root is None:
    return
  res.append(root.data)
  if(limit != 0):
    DLSUtil(root.left,limit-1)
    DLSUtil(root.right,limit-1)

def DLS(root,limit,goal):
  DLSUtil(root,limit)
  for x in res:
    print(x,end=' ')
    if(x == goal):
      return


def IDS(root,lim,goal):
  for i in range(lim+1):
    print("\n")
    res.clear()
    print("Iteration ",i+1,":")
    DLS(root,i,goal)
 


n=int(input("Enter the value of n:"))
start=int(input("Enter the starting value:"))
end=int(input("Enter the ending value:"))
list=random.sample(range(start,end),n) 
print("\nThe generated sequence is:")
for ele in list:
  print(ele,end=' ')
print("\n")
nodes=[None if ele is None else BT.Node(ele) for ele in list]
root=BT.constructBT(nodes)
print("State space tree representation of the sequence (binary tree):\n")
BT.printBT(root)
lim=int(input("Enter the limit for DLS (Depth Limited Search):"))
goal=int(input("Enter the goal state for DLS:"))
DLS(root,lim,goal)
lim2=int(input("\nEnter the limit for IDS (Iterative Deepening Search):"))
goal2=int(input("Enter the goal state for IDS:"))
IDS(root,lim2,goal2)
print("\n")

