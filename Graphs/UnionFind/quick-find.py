class QuickFind:
    def __init__(self, numNodes):
        # Maintain an array with component id
        # Component id represents which connected component a node belongs to
        # To start, assume every node is it's own component
        # component_id[node] = node
        self.n = numNodes
        self.component_id = [i for i in range(numNodes)]
        self.components = numNodes

    def quick_find(self, u, v):
        # For each incoming edge (u, v) check if component_id[u] != component_id[u] and update it to component_id[v]
        # FIND O(1)
        if self.component_id[u] != self.component_id[v]:
            old_id = self.component_id[v]
            # UNION O(n^2)
            for v in range(self.n):
                if self.component_id[v] == old_id:
                    self.component_id[v] = self.component_id[u]
            self.components -= 1

    def get_components(self):
        return self.components

# n is number of nodes, m is number of edges
# Max number of union ops = n - 1
# Max number of find ops = 2*m - undirected graph
# Overall Complexity: ~O(n^2)


edges = [[0, 1], [1, 2], [3, 4]]
numNodes = 5
uf = QuickFind(5)
for u, v in edges:
    uf.quick_find(u, v)
print(uf.get_components())
