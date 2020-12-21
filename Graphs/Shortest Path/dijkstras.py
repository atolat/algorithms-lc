# Dijkstra's Algorithm to find the minimum cost path from source node to destination node in a directed graph.
# Based on Prim's algorithm.
from heapq import *

class Solution(object):
    def minimumCost(self, N, connections, src, dst):
        """
        :type N: int
        :type connections: List[List[int]]
        :rtype: int
        """
        # Dijkstra's's Algorithm
        # Build Graph
        # Append node and asssociated cost to adjacency list
        adjList = {i: [] for i in range(1, N+1)}
        for u, v, cost in connections:
            adjList[u].append((v, cost))

        # Array to keep track of captured nodes
        captured = [0 for _ in range(N+1)]
        
        # Mark the source as captured
        captured[src] = 1

        # initialize priority queue to track min cost edges
        pq = []

        # Add all neighbors of src along with cost to pq
        for neighbor, cost in adjList[src]:
            heappush(pq, (cost, neighbor))

        # Similar to BFS, add min cost edges from pq to graph
        while pq:
            priority, node = heappop(pq)

            # If a node is already captured, we don't want to re-insert it in the PQ
            if captured[node] == 1:
                continue
            # Mark node as captured
            captured[node] = 1

            # Add the un-captured neighbors to the pq
            for (nei, nei_priority) in adjList[node]:
                if captured[nei] == 0:
                    # The updated priority of the node is the distance of node from src + neighbor's current priority
                    heappush(pq, (distance[node] + nei_priority, nei))

        # Check of all nodes are captured, return total cost
        return distance[dst]
