from queue import Queue
# Build the adjacency list

# Given edge list = [[s1,d1],[s2,d2],...]
edgeList = [[1,2],[2,4],[1,3],[2,3]]

# Given # of vertices n
adjList = [[] for _ in range(n)]
visited = [-1] * n
parent = [-1] * n
distance = [-1] * n

for [src,dst] in edgeList:
    adjList[src].append(dst)
    # For undirected graph
    adjList[dst].append(src)
     
# BFS
def bfs(source):
    q = Queue()
    visited[source] = 1
    distance[source] = 0
    q.put(source)

    while q.empty() is False:
        node = q.get()

        for neighbor in adjList[node]:
            if visited[neighbor] == -1:
                visited[neighbor] = 1
                parent[neighbor] = node
                distance[neighbor] = distance[node] + 1
                q.put(neighbor)
            else: # Detect cross edge
                if neighbor != parent[node]:
                    # Cross Edge Found!
                    if distance[neighbor] == distance[node]:
                        # Same level cross edge -> odd length cycle -> graph is not bipartite
# DFS
def dfs(source):
    visited[source] = 1
    for neighbor in adjList[source]:
        if visited[neighbor] == -1:
            parent[neighbor] = source
            dfs(neighbor)
        else: # Detect back edge
            if neighbor != parent[source]:
                # Back edge detected

# Outer Loop
components = 0
for v in range(n):
    if visited[v] == -1:
        components += 1   
        bfs(v)

return components