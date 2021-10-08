from collections import deque

from numba import jit, int64
from numba.typed import List

from My_Profiler import profile


class Graph:

    def __init__(self, edges, num_of_vertices: int):
        # initialize adj list
        self.level = 0
        self.adjList = [[] for _ in range(num_of_vertices)]
        self.numOfvertices = num_of_vertices

        # populate the graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)

    def __str__(self):
        return f'Num of vertices:{self.numOfvertices}, Edges are:{self.adjList}'

    # @profile
    def iterative_dfs(self, i_source: int):
        #print(vars(self))
        #x = vars(self)

        visited = set()
        stack = list()

        stack.append(i_source)

        print("--- ITERATIVE DFS ---")

        current = 0
        while len(stack):
            current = stack.pop()

            if current not in visited:
                visited.add(current)

                # Do something with the current
                # print(current)

                for v in self.adjList[current]:
                    if v not in visited:
                        stack.append(v)

        #temp = [1, 2, 3, 4]
        #x['adjList'].append(temp)

    #
    def bfs(self, i_source: int):
        _dq = deque()
        visited = set()

        _dq.append(i_source)

        while len(_dq):
            current = _dq.popleft()

            # Do something with the current
            # print(f'node is {current}, level: {self.level}')

            if current not in visited:
                visited.add(current)

                # visit current
                print(current)

                for v in self.adjList[current]:

                    if v not in visited:
                        _dq.append(v)

            self.level += 1


#
def _dfs(adj_list, i_source: int):

    visited = set()
    stack = list()

    stack.append(i_source)

    #print("--- ITERATIVE DFS ---")

    current = 0
    while len(stack):
        current = stack.pop()

        if current not in visited:
            visited.add(current)

            # Do operation on current
            #print(current)

            for v in adj_list[current]:
                if v not in visited:
                    stack.append(v)


class GraphNumba:

    def __init__(self, edges, num_of_vertices: int):
        # initialize adj list
        self.level = 0
        self.adjList = [[] for _ in range(num_of_vertices)]

        # populate the graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)

        # populate the graph 2
        self.adjList2 = List()
        for i in range(num_of_vertices):
            inner = List()
            for j in self.adjList[i]:
                inner.append(j)
            self.adjList2.append(inner)

    #
    # @profile
    def iterative_dfs_numba_wrapper(self, i_source: int):
        # _dfs(self.adjList2, i_source)

        _dfs_jit = jit(nopython=True)(_dfs)
        _dfs_jit(self.adjList2, i_source)

    @jit()
    def iterative_dfs(self, i_source: int):
        print(vars(self))
        visited = set()
        stack = list()

        stack.append(i_source)

        print("--- ITERATIVE DFS ---")

        current = 0
        while len(stack):
            current = stack.pop()

            if current not in visited:
                visited.add(current)

                # Do something with the current
                print(current)

                for v in self.adjList[current]:
                    if v not in visited:
                        stack.append(v)

    #
    @jit()
    def bfs(self, i_source: int):
        _dq = deque()
        visited = set()

        _dq.append(i_source)

        while len(_dq):
            current = _dq.popleft()

            # Do something with the current
            # print(f'node is {current}, level: {self.level}')

            if current not in visited:
                visited.add(current)

                # visit current
                print(current)

                for v in self.adjList[current]:

                    if v not in visited:
                        _dq.append(v)

            self.level += 1