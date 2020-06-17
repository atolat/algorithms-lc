# 973. K Closest Points to Origin
# Medium

# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

# (Here, the distance between two points on a plane is the Euclidean distance.)

# You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)


# Example 1:

# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
# Example 2:

# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]
# (The answer [[-2,4],[3,3]] would also be accepted.)


# Note:

# 1 <= K <= points.length <= 10000
# -10000 < points[i][0] < 10000
# -10000 < points[i][1] < 10000

# Solved using quick select ~ Lomuto's Partitioning 
# Complexity Analysis
# Time Complexity: O(N) in average case complexity, where N is the length of points.
# Space Complexity: O(N)

import math
import random


def kClosest(points, K):
    return helper(points, 0, len(points)-1, K-1)


def helper(a, start, end, index):
    # Base Case
    if a[start] == a[end]:
        return a[:start+1]

    # Lomuto's Partitioning
    random_pivot_index = random.randint(start, end)
    pivot = a[random_pivot_index]
    a[start], a[random_pivot_index] = a[random_pivot_index], a[start]

    orange = start
    green = start

    for green in range(start+1, end+1):
        if dist(a[green]) <= dist(pivot):
            orange += 1
            a[orange], a[green] = a[green], a[orange]
    a[orange], a[start] = a[start], a[orange]

    if orange == index:
        return a[:orange+1]
    elif index > orange:
        return helper(a, orange+1, end, index)
    else:
        return helper(a, start, orange-1, index)


def dist(point):
    return math.sqrt((point[0]**2)+(point[1]**2))


print(kClosest([[0, 1], [1, 0]], 1))


# Alternate Solution - using inbuilt sort
# Complexity Analysis
# Time Complexity: O(NlogN), where N is the length of points.
# Space Complexity: O(N)
def kClosest(self, points, K):
        points.sort(key=lambda P: P[0]**2 + P[1]**2)
        return points[:K]
    
# Alternate Solution - using MAXHEAP
from heapq import *
def kClosest(points, K):
    """
    :type points: List[List[int]]
    :type K: int
    :rtype: List[List[int]]
    """
    def distance_from_origin(point):
        x, y = point[0], point[1]
        return -(x*x + y*y)
    
    maxheap = []
    output = []
    
    for i in range(K):
        heappush(maxheap, (distance_from_origin(points[i]), points[i]))
    
    for i in range(K, len(points)):
        top = -(maxheap[0][0])
        if -distance_from_origin(points[i]) < top:
            heappop(maxheap)
            heappush(maxheap, (distance_from_origin(points[i]), points[i]))

    for i in range(len(maxheap)):
        output.append(maxheap[i][1])
        
    return output

# Time complexity #
# The time complexity of this algorithm is (N*logK) as we iterating all points and pushing them into the heap.

# Space complexity #
# The space complexity will be O(K) because we need to store ‘K’ point in the heap.