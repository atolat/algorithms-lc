from queue import Queue
def zombieMatrix(grid):
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
                if val == 1:
                    q.put((r,c,0))
                    
        # BFS
        while q.empty() is False:
            r,c,d = q.get()
            for nr, nc in getNeighbors(r,c,ROW,COLUMN):
                if grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    q.put((nr,nc,d+1))
        
        if any(0 in row for row in grid):
            return -1
        
        return d
    
# Alternate Solution
def minHour(self, rows, columns, grid):
    if not rows or not columns:
        return 0
    
    q = [[i,j] for i in range(rows) for j in range(columns) if grid[i][j]==1]
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    time = 0
    
    if not q:
        return -1

    while True:
        new = []
        for [i,j] in q:
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < rows and 0 <= nj < columns and grid[ni][nj] == 0:
                    grid[ni][nj] = 1
                    new.append([ni,nj])
        q = new
        if not q:
            break
        time += 1
        
    return time
                      
# Time Complexity: O(N)O(N), where NN is the number of cells in the grid.

# Space Complexity: O(N)O(N)