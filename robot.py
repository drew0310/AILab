from robotutil import *


class Graph:
   

    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.connect1(b, a, dist)

    def connect(self, A, B, distance=1):
        self.connect1(A, B, distance)
        if not self.directed:
            self.connect1(B, A, distance)

    def connect1(self, A, B, distance):
        self.graph_dict.setdefault(A, {})[B] = distance

    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        return links if b is None else links.get(b)

    def nodes(self):
        s1 = set(list(self.graph_dict.keys()))
        s2 = {k2 for v in self.graph_dict.values() for k2, v2 in v.items()}
        nodes = s1.union(s2)
        return list(nodes)


def UndirectedGraph(graph_dict=None):
    return Graph(graph_dict=graph_dict, directed=False)


class Problem:

    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        # TODO
        # Return a list of actions that can be executed in the given state.
        # or Yeild one action at a time
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def goal_test(self, state):
        if isinstance(self.goal, list):
            return any(x is state for x in self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return c + 1


class Node:

    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return f"<Node {self.state}>"

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        return Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))

    def solution(self):
        return [node.action for node in self.path()[1:]]

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)


def best_first_graph_search(problem, heur, display=False):
    # f = memoize(f, 'f')
    f = heur
    node = Node(problem.initial)
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    explored = set()
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            if display:
                print(len(explored), "paths have been expanded and",
                      len(frontier), "paths remain in the frontier")
            return node
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
    return None


greedy_best_first_graph_search = best_first_graph_search     # f(n) = h(n)


def astar_search(problem, display=False):
  h = manhattan_distance

    # h = memoize(h or problem.h, 'h')
  return best_first_graph_search(problem, lambda n: n.path_cost + h((n.state[0], n.state[1]), (problem.goal[0], problem.goal[1])), display)


class GraphProblem(Problem):

    def __init__(self, initial, goal, graph):
        super().__init__(initial, goal)
        self.graph = graph

    def actions(self, A):
        return list(self.graph.get(A).keys())

    def result(self, state, action):
        return action

    def path_cost(self, cost_so_far, A, action, B):
        return cost_so_far + (self.graph.get(A, B) or np.inf)

    def find_min_edge(self):
        m = np.inf
        for d in self.graph.graph_dict.values():
            local_min = min(d.values())
            m = min(m, local_min)

        return m

    def z(self, node):
        if locs := getattr(self.graph, 'locations', None):
            if type(node) is str:
                return int(distance(locs[node], locs[self.goal]))

            return int(distance(locs[node.state], locs[self.goal]))
        else:
            return np.inf

# Maze Application
# 3x3 Maze


states = [(x, y) for x in range(1, 4) for y in range(1, 4)]
barriers = int(input("Enter the number of barriers: "))
barrier_states = [tuple(
    map(int, input("Enter the barrier state: ").split())) for _ in range(barriers)]

goal_state = tuple(map(int, input("Enter the goal state: ").split()))
initial_state = tuple(map(int, input("Enter the initial state: ").split()))

graph = UndirectedGraph({s: {} for s in states})
for (x, y) in states:
    if (x, y) not in barrier_states:
        if x < 3:
            graph.connect((x, y), (x + 1, y), distance=int(
                input(f"Enter the distance between ({x}, {y}) and ({x + 1}, {y}): ")))

        if y > 1:
            graph.connect((x, y), (x, y - 1), distance=int(
                input(f"Enter the distance between ({x}, {y}) and ({x}, {y - 1}): ")))

graph.locations = {s: s for s in states}

print("A Star Search")
problem = GraphProblem(initial_state, goal_state, graph)
node = astar_search(problem)
print(initial_state, end='')
print(node.solution())
print("Path Cost: ", node.path_cost)


print("Greedy Best First Search")
problem = GraphProblem(initial_state, goal_state, graph)
node = greedy_best_first_graph_search(problem, lambda n: manhattan_distance((n.state[0], n.state[1]), (problem.goal[0], problem.goal[1])))
print(initial_state, end='')
print(node.solution())
print("Path Cost: ", node.path_cost)
