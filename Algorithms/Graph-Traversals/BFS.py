# Breadth-First-Traversal of Graph - Directed or Undirected graph??

from collections import deque

def bfs(graph, root):

    visited, queue = set(), deque([root])
    visited.add(root)

    while queue:
        currentNode = queue.popleft()
        
        print(currentNode)

        for neighbour in graph[currentNode]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

graph = {0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 2]}
print(bfs(graph, 0))
