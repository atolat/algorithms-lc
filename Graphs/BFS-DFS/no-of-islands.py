# 200. Number of Islands
# Medium

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

# Time Complexity: O(m*n)
# Space Complexity: O(m*n) - DFS, O(min(m,n)) - BFS.
# Approach: Our goal here is to count the number of connected components in the graph. Do a DFS or BFS traversal on the graph starting from the first node whose value is "1". Mark each node as "X" (visited). Explore all the nodes in the grid. After every DFS/BFS call from a node, if there are remaining nodes with "1", this indicates a new connected component. 
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        components = 0
        q = collections.deque()
        ROW = len(grid)
        if len(grid) > 0:
            COLUMN = len(grid[0])
        else:
            COLUMN = 0
                    
        def getNeighbors(r, c, ROW, COLUMN):
        # ((up), (left), (down), (right))
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < ROW and 0 <= nc < COLUMN:
                # use yield to make this function a generator (one time iterable)
                    yield nr, nc
        # BFS Approach
        def bfs(vertex):
            q.append(vertex)
            r,c = vertex
            grid[r][c] = 0
            while q:
                r,c = q.popleft()
                for nr, nc in getNeighbors(r, c, ROW, COLUMN):
                    if grid[nr][nc] == "1":
                        grid[nr][nc] = "X"
                        q.append((nr,nc))
            
        
        # DFS Approach
        def dfs(vertex):
            r,c = vertex
            grid[r][c] = "X"
            for nr,nc in getNeighbors(r,c,ROW,COLUMN):
                if grid[nr][nc] == "1":
                    dfs((nr,nc))
    
        for r,row in enumerate(grid):
            for c,val in enumerate(row):
                if val == "1":
                    components += 1
                    dfs((r,c)) # Alternatively bfs((r, c))                    
                    
        return components