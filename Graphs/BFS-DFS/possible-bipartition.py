# 886. Possible Bipartition
# Medium

# 1216

# 35

# Add to List

# Share
# Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

# Each person may dislike some other people, and they should not go into the same group.

# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

# Return true if and only if it is possible to split everyone into two groups in this way.


# Example 1:

# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]
# Example 2:

# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
# Example 3:

# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false

class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(N+1)]

        # Build adjaccency list
        for [src, dst] in dislikes:
            graph[src].append(dst)
            graph[dst].append(src)

        visited = [False for _ in range(N+1)]
        distance = [-1 for _ in range(N+1)]
        parent = [-1 for _ in range(N+1)]

        def bfs(source):
            # BFS will return True if an odd length cycle exists
            q = collections.deque([source])
            visited[source] = 1
            distance[source] = 0

            while q:
                # Get current node
                node = q.popleft()

                # Visit Neighbors
                for neighbor in graph[node]:
                    # Add unvisited neighbors to bfs queue
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        parent[neighbor] = node
                        distance[neighbor] = distance[node] + 1
                        q.append(neighbor)
                    else:  # node previously visited
                        if neighbor != parent[node]:  # Cross Edge
                            # If the node and neighbor are at the same level, the cross edge forming the cycle results in an odd length cycle - Not bipartite!
                            if distance[neighbor] == distance[node]:
                                return True
            return False

        for v in range(1, len(visited)):
            if not visited[v]:
                if bfs(v):  # Odd length cycle exists, bipartition not possible
                    return False

        return True
