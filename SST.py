class Node:
    def __init__(self, state, parent=None, limit=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.limit = limit


    def addChild(self, child):
        self.children.append(child)

    def getChildren(self):
        return self.children

    def getParent(self):
        return self.parent

    def getState(self):
        return self.state

    def __str__(self):
        return str(self.state)

    def __repr__(self):
        return str(self.state)


def constructStateSpaceTree(initialState, goalState, actions):
    root = Node(initialState)
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.state == goalState:
            return node
        for action in actions:
            child = Node(action(node.state), node)
            node.addChild(child)
            queue.append(child)
    return None


def printPath(node):
    if node is None:
        return
    printPath(node.getParent())
    print(f" Parent : {node.getParent()}", end=" ")
    print(node.getState())

def printNode(node):
    if not Node:
        print(f"Sate is {node.state}")
        print(f"Parnt : {node.parent.state}")
        print(f"Level is: {node.limit}")

# def isGoal():
#     return (2, 0) or (2, 1) or (2, 2) or (2, 3) or (2, 4)

# def main():
#     initialState = (0, 0)
#     goalState = [(2, 0), (4, 2)]
#     actions = [lambda state: (4, state[1]), lambda state: (state[0],3), lambda state: (0, state[1]), lambda state: (state[0], 0), lambdastate: (
#         state[0] - min(state[0], 3 - state[1]), state[1] +min(state[0], 3 - state[1])), lambda state: (state[0] + min(state[1],4 - state[0]), state[1] - min(state[1], 4 - state[0]))]
#     for goal in goalState:
#         node = constructStateSpaceTree(initialState, goal, actions)
#         if node is not None:
#             printPath(node)
#             print()

# if __name__ == "__main__":
#     main()



def nextState(state):
    return [lambda state: (4, state[1]), lambda state: (state[0], 3),
lambda state: (0, state[1]), lambda state: (state[0], 0), lambda
state: (
        state[0] - min(state[0], 3 - state[1]), state[1] +
min(state[0], 3 - state[1])), lambda state: (state[0] + min(state[1],
4 - state[0]), state[1] - min(state[1], 4 - state[0]))]
