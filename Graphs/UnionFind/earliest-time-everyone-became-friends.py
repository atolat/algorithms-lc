# 1101. The Earliest Moment When Everyone Become Friends
# Medium

# In a social group, there are N people, with unique integer ids from 0 to N-1.

# We have a list of logs, where each logs[i] = [timestamp, id_A, id_B] contains a non-negative integer timestamp, and the ids of two different people.

# Each log represents the time in which two different people became friends.  Friendship is symmetric: if A is friends with B, then B is friends with A.

# Let's say that person A is acquainted with person B if A is friends with B, or A is a friend of someone acquainted with B.

# Return the earliest time for which every person became acquainted with every other person. Return -1 if there is no such earliest time.


# Example 1:

# Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], N = 6
# Output: 20190301
# Explanation:
# The first event occurs at timestamp = 20190101 and after 0 and 1 become friends we have the following friendship groups [0,1], [2], [3], [4], [5].
# The second event occurs at timestamp = 20190104 and after 3 and 4 become friends we have the following friendship groups [0,1], [2], [3,4], [5].
# The third event occurs at timestamp = 20190107 and after 2 and 3 become friends we have the following friendship groups [0,1], [2,3,4], [5].
# The fourth event occurs at timestamp = 20190211 and after 1 and 5 become friends we have the following friendship groups [0,1,5], [2,3,4].
# The fifth event occurs at timestamp = 20190224 and as 2 and 4 are already friend anything happens.
# The sixth event occurs at timestamp = 20190301 and after 0 and 3 become friends we have that all become friends.

class UnionFind:
    def __init__(self, numNodes):
        # Maintain an array with component id
        # Component id represents which connected component a node belongs to
        # To start, assume every node is it's own component
        # parent[node] = node
        self.n = numNodes
        self.parent = [i for i in range(numNodes)]
        self.size = [1 for _ in range(numNodes)]
        self.components = numNodes

    # FIND - O(log n)
    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def quick_union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        # UNION O(1)
        if root_u != root_v:
            if self.size[root_u] < self.size[root_v]:
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            else:
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]
            self.components -= 1

    def get_components(self):
        return self.components


class Solution(object):
    def earliestAcq(self, logs, N):
        """
        :type logs: List[List[int]]
        :type N: int
        :rtype: int
        """
        logs.sort()
        uf = UnionFind(N)
        for time, u, v in logs:
            uf.quick_union(u, v)
            if uf.get_components() == 1:
                return time

        return -1
