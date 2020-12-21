# 1135. Connecting Cities With Minimum Cost
# Medium

# There are N cities numbered from 1 to N.

# You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and city2 together.  (A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)

# Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1) that connects those two cities together.  The cost is the sum of the connection costs used. If the task is impossible, return -1.

# Example 1:

# Input: N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
# Output: 6
# Explanation:
# Choosing any 2 edges will connect all cities so we choose the minimum 2.
# Example 2:

# Input: N = 4, connections = [[1,2,3],[3,4,4]]
# Output: -1
# Explanation:
# There is no way to connect all cities even if all edges are used.

# Note:

# 1 <= N <= 10000
# 1 <= connections.length <= 10000
# 1 <= connections[i][0], connections[i][1] <= N
# 0 <= connections[i][2] <= 10^5
# connections[i][0] != connections[i][1]

# Kruskal's Algorithm
# Greedy algorithm to build a MST. Built on top of Union Find. Rerpetitively add eddges to nodes in increasing order of cost if they don't form a cycle. When the number of components == 1, return the total cost.

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
        self.total_cost = 0

    # FIND with path compression - O(log n)
    # Amortized complexity of find with path compression is "practically constant".
    def find(self, x):
        # Base Case
        if x == self.parent[x]:
            return x

        # Recursive Case
        root_x = self.find(self.parent[x])
        self.parent[x] = root_x
        return root_x

    def quick_union(self, u, v, cost):
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
            self.total_cost += cost

    def get_components(self):
        return self.components

    def get_cost(self):
        return self.total_cost


class Solution(object):
    def minimumCost(self, N, connections):
        """
        :type N: int
        :type connections: List[List[int]]
        :rtype: int
        """
        # Sort list by costs
        connections.sort(key=lambda x: x[2])

        # Initialize Union Find
        uf = UnionFind(N)

        for u, v, cost in connections:
            uf.quick_union(u-1, v-1, cost)
            if uf.get_components() == 1:
                return uf.get_cost()

        return -1
