# 323. Number of Connected Components in an Undirected Graph
# Medium
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

# Example 1:

# Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

#      0          3
#      |          |
#      1 --- 2    4 

# Output: 2
# Example 2:

# Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

#      0           4
#      |           |
#      1 --- 2 --- 3

# Output:  1
# Note:
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

from Queue import Queue
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Build the Adjacency list
        adjList = [[] for _ in range(n)]
        visited = [-1] * n
        for [src,dst] in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
            
        def bfs(source):
            visited[source] = 1
            q = Queue()
            q.put(source)
            
            while q.empty() is False:
                node = q.get()
                
                for neighbor in adjList[node]:
                    if visited[neighbor] == -1:
                        q.put(neighbor)
                        visited[neighbor] = 1
        def dfs(source):
            visited[source] = 1
            for neighbor in adjList[source]:
                if visited[neighbor] == -1:
                    dfs(neighbor)
                        
        components = 0
        for v in range(n):
            if visited[v] == -1:
                components += 1
                dfs(v)
                
        return components