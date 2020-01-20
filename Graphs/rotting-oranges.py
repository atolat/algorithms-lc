# 994. Rotting Oranges
# Easy

# In a given grid, each cell can have one of three values:

# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

# Example 1:



# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

from Queue import Queue
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def getNeighbors(r, c, ROW, COLUMN):
        # ((up), (left), (down), (right))
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < ROW and 0 <= nc < COLUMN:
                # use yield to make this function a generator (one time iterable)
                    yield nr, nc

        # Initialize queue
        q = Queue()
        d = 0
        ROW = len(grid)
        COLUMN = len(grid[0])
        
        # Populate queue with verices -> 2
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    q.put((r,c,0))
                    
        # BFS
        while q.empty() is False:
            r,c,d = q.get()
            for nr, nc in getNeighbors(r,c,ROW,COLUMN):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.put((nr,nc,d+1))
        
        if any(1 in row for row in grid):
            return -1
        
        return d
    
                      
print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))