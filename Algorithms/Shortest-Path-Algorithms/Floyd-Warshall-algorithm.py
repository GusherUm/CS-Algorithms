class Solution:
    def findTheCity(self, n: int, edges, distanceThreshold: int) -> int:
        
        # All pair shortest path

        dist = [ [ float('inf') for j in range(n) ] for i in range(n) ]

        for i in range(n):
            dist[i][i] = 0

        for i, j, k in edges:
            dist[i][j] = dist[j][i] = k

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # Shortest path computed

        mn = n
        res = -1

        for i in range(n):
            canReach = 0

            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    canReach += 1

            if canReach <= mn:
                mn = canReach
                res = i

        return res

obj = Solution()
print(obj.findTheCity( 4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]] , 4) )
