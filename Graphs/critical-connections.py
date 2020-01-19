# 1192. Critical Connections in a Network
# Hard

# There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

# A critical connection is a connection that, if removed, will make some server unable to reach some other server.

# Return all critical connections in the network in any order.

 

# Example 1:



# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.

class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        # Build adjList
        adjList = [[] for _ in range(n)]
        
        for (src,dst) in connections:
            adjList[src].append(dst)
            adjList[dst].append(src)
            
        # Initialize tracking arrays
        visited = [-1] * n
        timestamp = [0]
        arrival = [-1] * n
        departure = [-1] * n
        parent = [-1] * n
        oldestarrival = [-1] * n
        result = []
        
        def dfs(source):
            visited[source] = 1
            arrival[source] = timestamp[0]
            timestamp[0] += 1
            oldestarrival[source] = arrival[source]
            for neighbor in adjList[source]:
                if visited[neighbor] == -1:
                    parent[neighbor] = source
                    oldestarrival[source] = min(oldestarrival[source], dfs(neighbor))
                else:
                    if neighbor != parent[source]:
                        oldestarrival[source] = min(oldestarrival[source], arrival[neighbor])
            if oldestarrival[source] == arrival[source] and source != 0:
                result.append([source, parent[source]])
            departure[source] = timestamp[0]
            timestamp[0] += 1
            