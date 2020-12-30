# 529. Minesweeper
# Medium

# 761

# 601

# Add to List

# Share
# Let's play the minesweeper game (Wikipedia, online game)!

# You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

# Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

# If a mine ('M') is revealed, then the game is over - change it to 'X'.
# If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
# If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
# Return the board when no more squares will be revealed.


# Example 1:
# Input:

# [['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'M', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E']]

# Click : [3,0]

# Output:

# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]

# Example 2:
# Input:

# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]

# Click : [1,2]

# Output:

# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'X', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        # Directions to get neighbors
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0),
                (1, 1), (1, -1), (-1, 1), (-1, -1))

        # Edge Case
        if not board or len(board[0]) == 0:
            return []

        m = len(board)
        n = len(board[0])

        # If you click on a mine, update mine location to 'X' and exit
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        # Helper function to get number of mines surrounding a cell
        def get_mines(r, c):
            mines = 0
            for dir in dirs:
                nr = r + dir[0]
                nc = c + dir[1]
                if nr >= 0 and nr < m and nc >= 0 and nc < n and board[nr][nc] == 'M':
                    mines += 1
            return mines

        # BFS Approach
        def bfs(r, c):
            # Initialize a queue for BFS and add the first node - click
            q = collections.deque([(r, c)])
            # Mark it as visited - 'B'
            board[r][c] = 'B'
            while q:
                i, j = q.popleft()
                # Get number of mines surrounding cell
                mines = get_mines(i, j)

                # If there are mines in surrounding cells, update the board value
                # Do not explore neighbors - continue to next cell in queue
                if mines > 0:
                    board[i][j] = str(mines)
                    continue
                for dir in dirs:
                    nr = i + dir[0]
                    nc = j + dir[1]
                    # Explore unvisited neighbors marked 'E'
                    if nr >= 0 and nr < m and nc >= 0 and nc < n and board[nr][nc] == 'E':
                        q.append((nr, nc))
                        board[nr][nc] = 'B'
        # DFS Approach

        def dfs(r, c):
            # Base Case - if the cell is not within boundaries or cell is already visited - return
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] == 'B':
                return

            # Mark cell as visited
            board[r][c] = 'B'
            mines = get_mines(r, c)

            # If there are mines surrounding the cell, update cell
            # Do not explore neighbors - return
            if mines > 0:
                board[r][c] = str(mines)
                return

            # Logic
            # Explore all neighbors using DFS
            for dir in dirs:
                nr = r + dir[0]
                nc = c + dir[1]
                dfs(nr, nc)

        bfs(click[0], click[1])
        # dfs(click[0], click[1])
        return board
