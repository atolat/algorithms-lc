# 207. Course Schedule
# Medium

# There are a total of n courses you have to take, labeled from 0 to n-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# Example 1:

# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.

# Approach 1 - Using Arrival/Departure time
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Initialize visited, arrival, departure, parent arrays, adjList, timestamp
        n = numCourses
        adjList = [[] for _ in range(n)]
        visited = [-1] * n
        arrival = [-1] * n
        departure = [-1] * n
        timestamp = [0]
        
        # Construct the graph
        for (src,dst) in prerequisites:
            adjList[dst].append(src)
            
        # DFS
        def dfs(source):
            arrival[source] = timestamp[0]
            timestamp[0] += 1
            visited[source] = 1
            for neighbor in adjList[source]:
                if visited[neighbor] == -1:
                    if dfs(neighbor):
                        return True
                else:
                    if departure[neighbor] == -1: # departure is absent
                        return True
            departure[source] = timestamp[0]
            timestamp[0] += 1
            return False
        
        # Outer Loop
        for v in range(n):
            if visited[v] == -1:
                if dfs(v):
                    return False
        return True
    
# Approach 2
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Adj List and indegree map
        adjList = {i:[] for i in range(numCourses)}
        inDegree = {i:0 for i in range(numCourses)}
        
        # Build Graph
        for src, dst in prerequisites:
            adjList[src].append(dst)
            inDegree[dst] += 1
            
        # Find sources
        sources = collections.deque()
        for node in inDegree:
            if inDegree[node] == 0:
                sources.append(node)
            
        sortedOrder = []
        # BFS
        while sources:
            curr = sources.popleft()
            sortedOrder.append(curr)
            
            for child in adjList[curr]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
                    
        if len(sortedOrder) != numCourses:
            return False
        
        return True