# You have a map that marks the locations of treasure islands. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to one of the treasure islands.

# Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from one of the starting point (marked as S) of the map and can move one block up, down, left or right at a time. The treasure island is marked as X. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. Output the minimum number of steps to get to any of the treasure islands.

# Example:

# Input:
# [['S', 'O', 'O', 'S', 'S'],
#  ['D', 'O', 'D', 'O', 'D'],
#  ['O', 'O', 'O', 'O', 'X'],
#  ['X', 'D', 'D', 'O', 'O'],
#  ['X', 'D', 'D', 'D', 'O']]

# Output: 3
# Explanation:
# You can start from (0,0), (0, 3) or (0, 4). The treasure locations are (2, 4) (3, 0) and (4, 0). Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).

from queue import Queue
import sys
def treasureIsland(grid):
    
    ROW = len(grid)
    COLUMN = len(grid[0])
    minDist = sys.maxsize
    
    def getNeighbors(r, c, ROW, COLUMN):
        # ((up), (left), (down), (right))
        for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
            if 0 <= nr < ROW and 0 <= nc < COLUMN:
            # use yield to make this function a generator (one time iterable)
                yield nr, nc
                    
    # BFS
    def bfs(vertex):
        visited = set()
        r,c = vertex
        q = Queue()
        q.put((r,c,0))
        while q.empty() is False:
            rv,cv,d = q.get()
            for nr,nc in getNeighbors(rv,cv,ROW,COLUMN):
                if grid[nr][nc] == 'O' and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    q.put((nr,nc,d+1))
                if grid[nr][nc] == 'X':
                    visited.add((nr,nc))
                    return d+1
        return sys.maxsize   
    

    
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == 'S':
                minDist = min(bfs((r,c)),minDist)
    return minDist
                 
    

                
        
    
    





grid = [['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]

print(treasureIsland(grid))