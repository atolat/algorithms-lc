# Zombie Clusters

# There are zombies in Seattle. Some of them know each other directly. Others might know each other transitively, through others. For example, if zombies A<->B and B<->C know each other directly, then A and C know each other indirectly and all three belong to one cluster.
# Knowing which zombies know each other directly, find the number of the zombie clusters.
# Input is a square matrix where each cell, zombies[A][B], indicates whether zombie A knows zombie B directly.

#
# Complete the 'zombieCluster' function below.
#
# The function accepts STRING ARRAY as parameter.
#
from collections import defaultdict, deque
def zombieCluster(zombies):
    if not zombies:
        return 0
                
    visited = [-1]*len(zombies)   
    q = deque()
    
    def zombiesBFS(z):
        while q:
            z = q.popleft()
            visited[z] = 1
            for i in range(n):
                if visited[i] == -1 and zombies[z][i] == '1':
                    visited[i] = 1
                    q.append(i)
                
                
    components = 0        
    for i in range(len(visited)):
        if visited[i] == -1:
            q.append(i)
            components += 1
            zombiesBFS(i)
        
        
    return components  