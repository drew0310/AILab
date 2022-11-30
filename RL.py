INF = 9999

# state diagram
Graph = {
  'CSE': ['Audi','Admin'],
  'ECE': ['Canteen','Admin'],
  'Canteen': ['ECE','Audi'],
  'Audi': ['Canteen','CSE'],
  'Admin': ['CSE','ECE']
}
start = 'Canteen'
end = 'CSE'

# Importing the libraries
import numpy as np

# Setting the parameters gamma and alpha for the Q-Learning
gamma = 0.75
alpha = 0.9

# PART 1 - DEFINING THE ENVIRONMENT
# Defining the states
location_to_state = {'CSE': 0,
                     'ECE': 1,
                     'Canteen': 2,
                     'Audi': 3,
                     'Admin': 4
                     }

state_to_location = {state: location for location, state in location_to_state.items()}
# Defining the actions
actions = [0,1,2,3]

# Defining the rewards
def reward(Graph,start,end):
  reward_matrix = [[0,0,0,0,0],
                   [0,0,0,0,0],
                   [0,0,0,0,0],
                   [0,0,0,0,0],
                   [0,0,0,0,0]]
                
  for i in range(len(reward_matrix)):
    for j in range(len(reward_matrix[i])):
      if i == j:
        reward_matrix[i][j] = -5
      elif state_to_location[j] in Graph[state_to_location[i]]:
        if state_to_location[j] == end:
          reward_matrix[i][j] = 100
        else:
          reward_matrix[i][j] = 0
      else:
        reward_matrix[i][j] = -INF
    
  return np.array(reward_matrix)

R = reward(Graph,start,end)
# PART 2 - BUILDING THE AI SOLUTION WITH Q-LEARNING

# Making a mapping from the states to the locations


# Making a function that returns the shortest route from a starting to ending location
def route(states,starting_location, ending_location):
    R_new = np.copy(R)
    ending_state = location_to_state[ending_location]
    R_new[ending_state, ending_state] = 100
    Q = np.array(np.zeros([states,states]))
    for i in range(1000):
        current_state = np.random.randint(0,states)
        playable_actions = []
        for j in range(states):
            if R_new[current_state, j] >= 0:
                playable_actions.append(j)
        next_state = np.random.choice(playable_actions)
        TD = R_new[current_state, next_state] + gamma * Q[next_state, np.argmax(Q[next_state,])] - Q[current_state, next_state]
        Q[current_state, next_state] = Q[current_state, next_state] + alpha * TD
    route = [starting_location]
    next_location = starting_location
    while (next_location != ending_location):
        starting_state = location_to_state[starting_location]
        next_state = np.argmax(Q[starting_state,])
        next_location = state_to_location[next_state]
        route.append(next_location)
        starting_location = next_location
    return route

# Printing the final route
print('Reward Matrix:')
print(R)
print('Route:')
print(route(5,'Canteen', 'CSE'))
