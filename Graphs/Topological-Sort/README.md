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
def topological_sort(vertices, edges):
  sortedOrder = []
  if vertices <= 0:
    return sortedOrder

  # a. Initialize the graph
  inDegree = {i: 0 for i in range(vertices)}  # count of incoming edges
  graph = {i: [] for i in range(vertices)}  # adjacency list graph

  # b. Build the graph
  for edge in edges:
    parent, child = edge[0], edge[1]
    graph[parent].append(child)  # put the child into it's parent's list
    inDegree[child] += 1  # increment child's inDegree

  # c. Find all sources i.e., all vertices with 0 in-degrees
  sources = deque()
  for key in inDegree:
    if inDegree[key] == 0:
      sources.append(key)

  # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
  # if a child's in-degree becomes zero, add it to the sources queue
  while sources:
    vertex = sources.popleft()
    sortedOrder.append(vertex)
    for child in graph[vertex]:  # get the node's children to decrement their in-degrees
      inDegree[child] -= 1
      if inDegree[child] == 0:
        sources.append(child)

  # topological sort is not possible as the graph has a cycle
  if len(sortedOrder) != vertices:
    return []

  return sortedOrder
```