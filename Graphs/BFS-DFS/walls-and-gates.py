# 286. Walls and Gates
# Medium

# 1419

# 22

# Add to List

# Share
# You are given a m x n 2D grid initialized with these three possible values.

# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

# Example:

# Given the 2D grid:

# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# After running your function, the 2D grid should be:

#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        def getNeighbors(r, c, ROW, COLUMN):
            # ((up), (left), (down), (right))
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < ROW and 0 <= nc < COLUMN:
                    # use yield to make this function a generator (one time iterable)
                    yield nr, nc

        q = collections.deque()
        for row in xrange(len(rooms)):
            for col in xrange(len(rooms[0])):
                if rooms[row][col] == 0:
                    q.append((row, col))

        while q:
            r, c = q.popleft()
            for nr, nc in getNeighbors(r, c, len(rooms), len(rooms[0])):
                if rooms[nr][nc] == 2147483647:
                    rooms[nr][nc] = rooms[r][c]+1
                    q.append((nr, nc))
