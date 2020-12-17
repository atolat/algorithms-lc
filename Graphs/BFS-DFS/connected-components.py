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

# Time Complexity: O(V+E)
# Space Complexity: O(N)
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Build the Adjacency list
        adjList = [[] for _ in range(n)]
        visited = set()
        for src,dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
            
        def bfs(source):
            visited[source] = 1
            q = collections.deque([source])
            
            while q:
                # get the current node
                node = q.popleft()
                visited.add(node)
                
                # visit the neighbors
                for neighbor in adjList[node]:
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
        
        def dfs(source):
            visited.add(source)
            for neighbor in adjList[source]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        # Outer Loop
        components = 0
        
        # nodes are numbered 0 to n-1
        for i in range(n):
            # if node is not visited, increment components and launch dfs/bfs with the node as source
            if i not in visited:
                components += 1
                dfs(i)
                
        return components
                    