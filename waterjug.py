jug1, jug2, aim = 4, 3, 2

def next(tuple):
  (a1,a2)=tuple
  list = []
  list.append((0, a2))
  list.append((a1, 0))
  list.append((jug1, a2))
  list.append((a1, jug2))
  list.append((a1 + min(a2, (jug1-a1)),
                a2 - min(a2, (jug1-a1))))
  list.append((a1, jug2) or(a1 - min(a1, (jug2-a2)),a2 + min(a1, (jug2-a2))))
  purelist =  [*set(list)]
  purelist.remove((a1,a2))
  return purelist

def nextwl(tuple):
  (a1,a2,a3)=tuple
  a3=a3+1
  list = []
  list.append((0, a2,a3))
  list.append((a1, 0,a3))
  list.append((jug1, a2,a3))
  list.append((a1, jug2,a3))
  list.append((a1 + min(a2, (jug1-a1)),
                a2 - min(a2, (jug1-a1)),a3))
  list.append((a1, jug2,a3) or(a1 - min(a1, (jug2-a2)),a2 + min(a1, (jug2-a2)),a3))
  purelist =  [*set(list)]
  if (a1,a2,a3) in purelist:
    purelist.remove((a1,a2,a3))
  if (a1,a2,a3+1) in purelist:
    purelist.remove((a1,a2,a3+1))
  return purelist

def bfs():
  set=[]
  queue=[(0,0)]
  i=0
  while len(queue) and (i<50):
    index=queue.pop(0)
    if index not in set:
      set.append(index)
      print(index,end=" ")
      if(index==(aim,0)): break
      Next = next(index)
      print("Neighbours= ",Next)
      queue.extend(Next)
    i=i+1
  print("\nGOAL REACHED")


def dfs():
  set=[]
  queue=[(0,0)]
  i=0
  while queue and (i<50):
    index=queue.pop()
    if index not in set:
      set.append(index)
      print(index,end=" ")
      if(index==(aim,0)): break
      Next = next(index)
      print("Neighbours= ",Next)
      queue.extend(Next)
    i=i+1
  print("\nGOAL REACHED")


def dls(limit):
  set=[]
  stack=[(0,0,1)]
  while stack:
    node = stack.pop()
    if (node[0]==aim and node[1]==0): 
      print("\nGOAL REACHED")
      return True
    if (node[0],node[1]) not in set and node[2] <= limit:
      set.append((node[0],node[1]))
      print(node, end=" ")
      Next = nextwl(node)
      for node in Next:
        if((node[0],node[1]) in Next):
          Next.remove((node[0],node[1]))
      print("Neighbours= ",Next)
      stack.extend(Next)
  return False


def ids(limits):
    for limit in range(limits):
        node = dls(limit)
        if node == True:
            return True
    return False

def main():
  print("BFS:")
  bfs()
  print()
  print("DFS:")
  dfs()
  print()
  print("DLS with Limit=6:")
  if(dls(6)!=True): print("NO SOLUTION")
  print()
  print("IDS (gives solution with limit=7):")
  if(ids(7)!=True): print("NO SOLUTION")
  print()

if __name__ == "__main__":
    main()
