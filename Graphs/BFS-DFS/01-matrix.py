# 542. 01 Matrix
# Medium

# 1938

# 117

# Add to List

# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.


# Example 1:

# Input:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]

# Output:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
# Example 2:

# Input:
# [[0,0,0],
#  [0,1,0],
#  [1,1,1]]

# Output:
# [[0,0,0],
#  [0,1,0],
#  [1,2,1]]

# Optimized BFS Approach
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)
# Approach: Start a BFS from all the '0' nodes by adding them to a queue along with a distance parameter. Mark the '1' nodes as -1.
# At every level of BFS, update the neighbors of '0' with the distance.
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def getNeighbors(r, c, ROW, COLUMN):
            # ((up), (left), (down), (right))
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < ROW and 0 <= nc < COLUMN:
                    # use yield to make this function a generator (one time iterable)
                    yield nr, nc

        ROW = len(matrix)
        COLUMN = len(matrix[0])
        q = collections.deque()
        for r in range(ROW):
            for c in range(COLUMN):
                if matrix[r][c] == 0:
                    # Append node coordinates and initial distance '1' for every 0 node
                    q.append((r, c, 1))
                else:
                    # Mark '1' as '-1'
                    matrix[r][c] = -1

        while q:
            r, c, d = q.popleft()
            for nr, nc in getNeighbors(r, c, ROW, COLUMN):
                if matrix[nr][nc] == -1:
                    # Update matrix value with distance
                    matrix[nr][nc] = d
                    # Add nodes back to queue with d+1
                    q.append((nr, nc, d+1))
        return matrix
