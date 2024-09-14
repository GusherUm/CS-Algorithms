def Dijkstra(n, graph, start):

    visited = set()

    adjMatrix = [ [ 0 for j in range(n) ] for i in range(n) ]

    for i, j, k in graph:
        adjMatrix[i][j] = adjMatrix[j][i] = k

    d = [ float('inf') for i in range(n) ]

    d[start] = 0
    queue = [start]

    while len(visited) < n:
        cur = queue.pop(0)
        visited.add(cur)

        for i in range(n):
            if i not in visited and adjMatrix[cur][i] > 0 and (d[cur] + adjMatrix[cur][i] < d[i]):
                visited.add(i)
                d[i] = d[cur] + adjMatrix[cur][i]
                queue.append(i)
        
    return d

graph = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
print(Dijkstra(4, graph, 0))
