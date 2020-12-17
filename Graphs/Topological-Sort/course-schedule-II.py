# 210. Course Schedule II
# Medium
# There are a total of n courses you have to take, labeled from 0 to n-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

# Example 1:

# Input: 2, [[1,0]] 
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
#              course 0. So the correct course order is [0,1] .
# Example 2:

# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
#              courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
#              So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
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
        topsort = []
        
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
            topsort.append(source)
            return False
        
        # Outer Loop
        for v in range(n):
            if visited[v] == -1:
                if dfs(v):
                    return []
        topsort.reverse()
        return topsort