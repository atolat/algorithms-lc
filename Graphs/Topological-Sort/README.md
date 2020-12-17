## Topological Sort

### Using Arrival/Departure Time
```python
# Auxillary arrays...
topsort = [] 
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


# Outer Loop
for v in range(n):
    if visited[v] == -1:
        if dfs(v):
            return []
topsort.reverse()
return topsort
```

### Kahn's Algorithm
```python
# Initialize graph
inDegree = [0 for _ in range(n)] # n is number of nodes
adjList = [[] for _ in range(n)] # n is number of nodesd

# Build Graph
for (dst, src) in edges:
    adjList[src].append(dst)
    inDegree[dst] += 1
    
# Collect sources
sources = collections.deque()
for i in range(len(inDegree)):
    if inDegree[i] == 0:
        sources.append(i)

sortedOrder = []
# BFS 
while sources:
    node = sources.popleft()
    sortedOrder.append(node)
    for child in adjList[node]:
        inDegree[child] -= 1
        if inDegree[child] == 0:
            sources.append(child)

return sortedOrder
```