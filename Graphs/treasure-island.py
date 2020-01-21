# You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to the treasure island.

# Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from the top-left corner of the map and can move one block up, down, left or right at a time. The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe. Output the minimum number of steps to get to the treasure.

# Example:

# Input:
# [['O', 'O', 'O', 'O'],
#  ['D', 'O', 'D', 'O'],
#  ['O', 'O', 'O', 'O'],
#  ['X', 'D', 'D', 'O']]

# Output: 5
# Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.

from queue import Queue

def treasureIsland(grid):
    ROW = len(grid)
    COLUMN = len(grid[0])
    
    def getNeighbors(r, c, ROW, COLUMN):
        # ((up), (left), (down), (right))
        for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
            if 0 <= nr < ROW and 0 <= nc < COLUMN:
            # use yield to make this function a generator (one time iterable)
                yield nr, nc
    
    q = Queue()
    d = 0
    q.put((0,0,d))
    
    # BFS
    while q.empty() is False:
        r,c,d = q.get()
        for nr,nc in getNeighbors(r,c,ROW,COLUMN):
            if grid[nr][nc] == 'O':
                grid[nr][nc] = 'D'
                q.put((nr,nc,d+1))
            if grid[nr][nc] == 'X':
                return d + 1
    return -1

grid = [['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

print(treasureIsland(grid))