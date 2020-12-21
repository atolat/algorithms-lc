# 743. Network Delay Time
# Medium

# There are N network nodes, labelled 1 to N.

# Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

# Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

# Example 1:
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
# Output: 2

class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        # Build Graph
        # Append node and asssociated cost to adjacency list
        adjList = collections.defaultdict(list)
        for u, v, cost in times:
            adjList[u].append((v, cost))

        # Array to keep track of captured nodes
        captured = [0 for _ in range(N+1)]
        distance = [0 for _ in range(N+1)]

        total_cost = 0

        # Start at node 1
        captured[K] = 1
        distance[K] = 0

        # initialize priority queue to track min cost edges
        pq = []

        # Add all neighbors of node 1 along with cost to pq
        for neighbor, cost in adjList[K]:
            heappush(pq, (cost, neighbor))

        # Similar to BFS, add min cost edges from pq to graph
        while pq:
            priority, node = heappop(pq)

            # If a node is already captured, we don't want to re-insert it in the PQ
            if captured[node] == 1:
                continue
            # Add to total cost and mark node as captured
            distance[node] = priority
            captured[node] = 1

            # Add the un-captured neighbors to the pq
            for (nei, nei_priority) in adjList[node]:
                if captured[nei] == 0:
                    heappush(pq, (distance[node] + nei_priority, nei))

        # Check of all nodes are captured, return total cost
        return max(distance) if max(distance) > 0 and sum(captured) == N else -1
