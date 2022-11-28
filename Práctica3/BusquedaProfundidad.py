from collections import deque
 
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
 
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def iterativeDFS(graph, v, discovered):
    stack = deque()
    stack.append(v)
 
    while stack:
        v = stack.pop()
        if discovered[v]:
            continue
        discovered[v] = True
        print(v, end=' ')
 
        adjList = graph.adjList[v]
        for i in reversed(range(len(adjList))):
            u = adjList[i]
            if not discovered[u]:
                stack.append(u)
 
 
if __name__ == '__main__':
    edges = [
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
    ]
 
    n = 13
    graph = Graph(edges, n)
    discovered = [False] * n

    for i in range(n):
        if not discovered[i]:
            iterativeDFS(graph, i, discovered)
 
