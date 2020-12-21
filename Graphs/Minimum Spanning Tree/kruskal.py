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
    
numNodes = 3
# List with edge uc,c v, cost
costs = [[1,2,5],[1,3,6],[2,3,1]]

# Sort list by costs
costs.sort(key = lambda x: x[2])

# Initialize Union Find 
uf = UnionFind(numNodes)

for u, v, cost in costs:
    uf.quick_union(u-1, v-1, cost)
    if uf.get_components() == 1:
        print(uf.get_cost())
        break     

    