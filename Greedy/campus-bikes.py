# 1057. Campus Bikes
# Medium

# On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is a 2D coordinate on this grid.
# Our goal is to assign a bike to each worker. Among the available bikes and workers, we choose the (worker, bike) pair with the shortest Manhattan distance between each other, and assign the bike to that worker. (If there are multiple (worker, bike) pairs with the same shortest Manhattan distance, we choose the pair with the smallest worker index; if there are multiple ways to do that, we choose the pair with the smallest bike index). We repeat this process until there are no available workers.
# The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

# Return a vector ans of length N, where ans[i] is the index (0-indexed) of the bike that the i-th worker is assigned to.

# Example 1:
# Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
# Output: [1,0]
# Explanation:
# Worker 1 grabs Bike 0 as they are closest (without ties), and Worker 0 is assigned Bike 1. So the output is [1, 0].

# Example 2:
# Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
# Output: [0,2,1]
# Explanation:
# Worker 0 grabs Bike 0 at first. Worker 1 and Worker 2 share the same distance to Bike 2, thus Worker 1 is assigned to Bike 2, and Worker 2 will take Bike 1. So the output is [0,2,1].

# TIME COMPLEXITY: O(W*B) -> W is number of workers, B is number of bikes
# SPACE COMPLEXITY: O(W*B)
# Approach - Use a map to keep track of distances and worker/bike pairs
# This solution does not require sorting the keys or using a sorted/ordered map
from collections import defaultdict


class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        # assigned keeps track of the bikes assigned so far
        assigned = [False for _ in range(len(bikes))]

        # Initialize result array with -1 to track workers that have not been assigned bikes
        result = [-1 for _ in range(len(workers))]

        # map to hold distances (manhattan distance between worker and bike) as keys with a list of pairs of workers and bikes
        _map = defaultdict(list)
        max_dist = 0

        # For every worker, bike pair, calculate the distance and append it to the list corresponding to that distance
        for worker_id, worker in enumerate(workers):
            for bike_id, bike in enumerate(bikes):
                dist = self.manhattan_dist(worker, bike)
                _map[dist].append((worker_id, bike_id))
                # Keep track of the max distance in the map
                # Use this to iterate over keys in the map
                # This eliminates the need to sort the keys or use a sorted map/Tree Map
                max_dist = max(max_dist, dist)
        count = 0
        # Iterate over all distances from 0 to max_distance
        for i in range(0, max_dist+1):
            if count == len(workers):
                break
            # If the key exists in the map and the corresponding list is not empty
            if i in _map and _map[i]:
                # get the list
                li = _map[i]
                # Iterate over every pair in the list and greedily assign bikes to workers that have not been assigned so far
                for worker_id, bike_id in li:
                    if not assigned[bike_id] and result[worker_id] == -1:
                        result[worker_id] = bike_id
                        assigned[bike_id] = True
                        count += 1
        return result

    # Function to compute manhattan distance between two points
    def manhattan_dist(self, p1, p2):
        return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
