# 261. Graph Valid Tree
# Medium

# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

# Example 1:

# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true
# Example 2:

# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false
# Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.

from Queue import Queue
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # BFS Traversal, 1 connected component, no cross edges -> valid tree
        
        # Step 1 - Construct the adjacency list from edges
        # Initialize empty adjList - list of lists
        adjList = [[] for _ in range(n)]
        
        # Initialize parent and visited arrays with -1
        visited = [-1] * n 
        parent = [-1] * n
        
        # Construct adjlist 
        for [src,dst] in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
            
        # Step 2 - BFS
        def bfs(source):
            # Initialize new queue
            q = Queue()
            # Push source on queue
            q.put(source)
            # Mark source as visited
            visited[source] = 1
            
            while q.empty() is False:
                # Pop vertex from queue and visit neighbors of popped vertex
                node = q.get()
                for neighbor in adjList[node]:
                    # if the neighbor is not visited, mark it as visited and push it on queue, mark it's parent as the popped vertex
                    if visited[neighbor] == -1:
                        visited[neighbor] = 1
                        parent[neighbor] = node
                        q.put(neighbor)
                    # if the neighbor is visited - this indicates a cross edge - we have to differenciate this from a single tree edge
                    # Ex - 1----2 => 1 can visit 2 and 2 can visit 1, but this is still a valid tree
                    else:
                        # If the parent of vertex that is popped is the neighbor, it is not a cross edge
                        # Q: Am I being re-visited by my parent? -- Possible since it's an undirected graph
                        # A: Yes, This is not a cross edge
                        # A: No, This is a cross edge -- results in a cycle
                        if neighbor != parent[node]:
                            # Cross edge found, component being explored has a cycle - return True
                            return True
            return False
        
        # Step 2a - Try with DFS
        def dfs(source):
            # Mark source as visited 
            visited[source] = 1
            # Explore neighbors of source
            for neighbor in adjList[source]:
                # If the neighbor is not visited, mark it as visited, set the parent as source and launch dfs on it, recursively!
                if visited[neighbor] == -1:
                    visited[neighbor] = 1
                    parent[neighbor] = source
                    dfs(neighbor)
                else:
                    # Vertex is visited, now check if it has been visited by it's parent
                    # If not, this is a back edge - cycle present in the component being visited!
                    if neighbor != parent[source]:
                        return True
            return False
        
        # Step 3 - Outer Loop, connected components
        components = 0
        for v in range(n):
            # Visit all the un-visited components
            if visited[v] == -1:
                components += 1
                # If components > 1 at any point, return False - NOT A VALID TREE
                if components > 1:
                    return False
                # if either bfs or dfs return True - component has a cycle - NOT A VALID TREE
                if dfs(v):
                    return False
        return True