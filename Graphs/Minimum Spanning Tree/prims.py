from heapq import *

class Solution(object):
    def minimumCost(self, N, connections):
        """
        :type N: int
        :type connections: List[List[int]]
        :rtype: int
        """
        # Prim's Algorithm
        # Build Graph
        # Append nodde and asssociated cost to adjacency list
        adjList = {i: [] for i in range(1, N+1)}
        for u, v, cost in connections:
            adjList[u].append((v, cost))
            adjList[v].append((u, cost))

        # Array to keep track of captured nodes
        captured = [0 for _ in range(N+1)]

        total_cost = 0

        # Start at node 1
        captured[1] = 1

        # initialize priority queue to track min cost edges
        pq = []

        # Add all neighbors of node 1 along with cost to pq
        for neighbor, cost in adjList[1]:
            heappush(pq, (cost, neighbor))

        # Similar to BFS, add min cost edges from pq to graph
        while pq:
            priority, node = heappop(pq)

            # If a node is already captured, we don't want to re-insert it in the PQ
            if captured[node] == 1:
                continue
            # Add to total cost and mark node as captured
            total_cost += priority
            captured[node] = 1

            # Add the un-captured neighbors to the pq
            for (nei, nei_priority) in adjList[node]:
                if captured[nei] == 0:
                    heappush(pq, (nei_priority, nei))

        # Check of all nodes are captured, return total cost
        return total_cost if sum(captured) == N else -1
