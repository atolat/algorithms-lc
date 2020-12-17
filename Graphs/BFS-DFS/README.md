## Eulerian Paths & Cycles
- The sum of degrees of all vertices in an undireccted graph = 2*|Edges|
- The sum of in-degrees + out-degrees in a directed graph = |Edges|
- Eulerian Cycle Problem: Determine whether a given undirected graph has a cycle that covers each edge exactly once.
- Eulerian Path: path that covers every edge of the graph exactly once.
- Hamiltonian Path: path that visits all vertices exactly once. (Hamiltonian Cycle Problem - NP hard)
- It is possible for a graph to have an Eulerian cycle even if it is disconnected - all the edges of the cycle must be a part of the same connected component.
- If the degree of any vertex is odd, the graph cannot have an Eulerian cycle - If a graph is connected, and the degree of every vertex is even, it has an Eulerian cycle.
- If the degree of start and end vertices is odd and every other intermediate vertex is even,the graph has an Eulerian Path. 
- It is IMPOSSIBLE for a graph to have a single vertex with an odd degree.
- It is IMPOSSIBLE for a graph to have an odd number of vertices with an odd degree.
- Number of verices with odd degree - 0 - graph has Eulerian Cycle
- Number of verices with odd degree - 2 - graph has Eulerian Path

## Traversals

### Auxillary Arrays
```python
# Keep track of visited nodes - array or set
visited = [-1] * n

# Keep track of parent nodes of current node
parent = [-1] * n

# Keep track of distance of a node from source - BFS
distance = [-1] * n

# Keep track of arrival and departure times for vertices
# Used to detect forward, backward and cross edges
arrival = [-1] * n
departure = [-1] * n
time = 0
```

### Build Adjacency List
```python
# Given edge list = [[s1,d1],[s2,d2],...]
edgeList = [[1,2],[2,4],[1,3],[2,3]]

# Given # of vertices n
adjList = [[] for _ in range(n)]

for src, dst in edgeList:
    adjList[src].append(dst)
    # For undirected graph
    adjList[dst].append(src)
```


### BFS
```python
def bfs(source):
    q = collections.deque()
    visited[source] = 1
    q.append(source)

    while q.empty() is False:
        node = q.popleft()

        for neighbor in adjList[node]:
            if visited[neighbor] == -1:
                visited[neighbor] = 1
                parent[neighbor] = node
                distance[neighbor] = distance[node] + 1
                q.append(neighbor)
            else: # Detect cross edge
                if neighbor != parent[node]:
                    pass
                    # Cross Edge Found!
                    if distance[neighbor] == distance[node]:
                        pass
       
```

### DFS
```python
def dfs(source):
    visited[source] = 1
    # For directed graph, record arrival and departure time at a node
    arrival[source] = time + 1
    for neighbor in adjList[source]:
        if visited[neighbor] == -1:
            parent[neighbor] = source
            dfs(neighbor)
        else: # Detect back edge
            if neighbor != parent[source]:
                pass
                # Back edge detected
            # Cases for directed graph - tree, forward, cross edge
            if departure[neighbor] == -1: # Departure time absent
                pass
                # Back edge, cycle exists
            elif arrival[source] > arrival[neighbor]:
                pass
                # Forward Edge found
            else: # arrival[source] < arrival[neighbor] and departure time of neighbor is set
                pass
                # Cross edge found
            
        departure[source] = time + 1 
```

### Outer Loop - Count Connected Components
```python
components = 0
for v in range(n):
    if visited[v] == -1:
        components += 1
        # dfs(v)
        # Handle boolean returns for cycles, back edges
        bfs(v)
```

### Get Neighbors in Adjacency Matrix
```python
def getNeighbors(r, c, ROW, COLUMN):
# ((up), (left), (down), (right))
    for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
        if 0 <= nr < ROW and 0 <= nc < COLUMN:
        # use yield to make this function a generator (one time iterable)
            yield nr, nc
```