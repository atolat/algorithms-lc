# 785. Is Graph Bipartite?
# Medium

# Given an undirected graph, return true if and only if it is bipartite.

# Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

# The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

# Example 1:
# Input: [[1,3], [0,2], [1,3], [0,2]]
# Output: true
# Explanation: 
# The graph looks like this:
# 0----1
# |    |
# |    |
# 3----2
# We can divide the vertices into two groups: {0, 2} and {1, 3}.
# Example 2:
# Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
# Output: false
# Explanation: 
# The graph looks like this:
# 0----1
# | \  |
# |  \ |
# 3----2
# We cannot find a way to divide the set of nodes into two independent subsets.
# Note:
# graph will have length in range [1, 100].
# graph[i] will contain integers in range [0, graph.length - 1].
# graph[i] will not contain i or duplicate values.
# The graph is undirected: if any element j is in graph[i], then i will be in graph[j].

from Queue import Queue
class Solution(object):
    def isBipartite(self, graph):
        # BFS Traversal, no odd length cycles - BIPARTITE
        n = len(graph)
        adjList = graph # graph is given as an adjacency list in the question
        
        # Initialize parent and visited arrays with -1
        visited = [-1] * n 
        parent = [-1] * n
        distance = [-1] * n
                    
        # Step 2 - BFS
        def bfs(source):
            # Initialize new queue
            q = Queue()
            # Push source on queue
            q.put(source)
            # Mark source as visited, distance as 0
            visited[source] = 1
            distance[source] = 0
            
            while q.empty() is False:
                # Pop vertex from queue and visit neighbors of popped vertex
                node = q.get()
                for neighbor in adjList[node]:
                    # if the neighbor is not visited, mark it as visited and push it on queue, mark it's parent as the popped vertex
                    if visited[neighbor] == -1:
                        visited[neighbor] = 1
                        parent[neighbor] = node
                        # One level down, increment distance of parent by 1
                        distance[neighbor] = distance[node] + 1
                        q.put(neighbor)
                    # if the neighbor is visited - this indicates a cross edge - we have to differenciate this from a single tree edge
                    # Ex - 1----2 => 1 can visit 2 and 2 can visit 1, but this is still a valid tree
                    else:
                        # If the parent of vertex that is popped is the neighbor, it is not a cross edge
                        # Q: Am I being re-visited by my parent? -- Possible since it's an undirected graph
                        # A: Yes, This is not a cross edge
                        # A: No, This is a cross edge -- results in a cycle
                        if neighbor != parent[node]:
                            # Cross edge found
                            if distance[node] == distance[neighbor]:
                                # If the cross edge is between node at the same level --> odd length cycle -> return True
                                return True
            return False
        
        
        # Step 3 - Outer Loop, connected components
        components = 0
        for v in range(n):
            # Visit all the un-visited components
            if visited[v] == -1:
                if bfs(v): # If any component has odd length cycles, it is not BIPRTITE
                    return False
        return True