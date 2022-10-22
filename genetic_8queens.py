import random
def fitnessFunction(state):
  fitness = 0
  for i in range(0, 7 + 1):
    for j in range(i + 1, 7 + 1):
      if (state[i] != state[j] and j - i != abs(state[i] - state[j])):
        fitness += 1
  return fitness


def view(li):
    print()

    for i in range(8):
        x = li[i]
        for j in range(8):
            if j == x:
                print('[Q]', end='')
            else:
                print('[ ]', end='')
        print()
    
    print()


def createChildren(parent1, parent2):
    state1 = parent1[2]
    state2 = parent2[2]
    parent1[1] -= 1
    parent2[1] -= 1
    #crossover
    child1 = [state1[0], state1[1], state1[2], state1[3],
             state2[4], state2[5], state2[6], state2[7]]
    child2 = [state2[0], state2[1], state2[2], state2[3],
             state1[4], state1[5], state1[6], state1[7]]
    #mutation
    pos = random.randint(0, 7)
    val = random.randint(0, 7)
    child1[pos] = val
    pos = random.randint(0, 7)
    val = random.randint(0, 7)
    child2[pos] = val
    return [fitnessFunction(child1), 0, child1], [fitnessFunction(child2), 0, child2]

def GA(states):
    loops=0
    while (states[0][0] < 28):
        loops += 1
        print("Loop : ", loops,"\tMaximum obtained fitness till now: ",states[0][0])

        for i in range(0, min(2, len(states) - 1), 2):
            parent1 = states[i]
            parent2 = states[i + 1]
            children1,children2 = createChildren(parent1, parent2)
        states.append(children1)
        states.append(children2)
        states.sort(reverse = True)
    print("\n\n!!!FOUND THE ANSWER!!!\nLoop : ", loops+1,"\tMaximum fitness: ",states[0][0])
    return states



K = 10
states = []
for i in range(K):
	state = [random.randint(0, 7) for j in range(8)]
	print(state)
	states.append([fitnessFunction(state), 0, state])
states.sort(reverse = True)
states=GA(states)
li = states[0][2]
print("Solution : ", li)
view(li)