class QuickUnion:
    def __init__(self, numNodes):
        # Maintain an array with component id
        # Component id represents which connected component a node belongs to
        # To start, assume every node is it's own component
        # parent[node] = node
        self.n = numNodes
        self.parent = [i for i in range(numNodes)]
        self.components = numNodes

    # FIND - O(n)
    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def quick_union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        # UNION O(1)
        if root_u != root_v:
            self.parent[root_v] = root_u
            self.components -= 1

    def get_components(self):
        return self.components

# n is number of nodes, m is number of edges
# Max number of union ops = n - 1
# Max number of find ops = 2*m - undirected graph
# Overall Complexity: ~O(n^2)


edges = [[0, 1], [1, 2], [3, 4]]
numNodes = 5
uf = QuickUnion(5)
for u, v in edges:
    uf.quick_union(u, v)
print(uf.get_components())
