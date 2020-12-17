# Knight's Tour On A Chess Board

# You are given a rows * cols chessboard and a knight that moves like in normal chess. Currently knight is at starting position denoted by start_row th row and start_col th col, and want to reach at ending position denoted by end_row th row and end_col th col. The goal is to calculate the minimum number of moves that the knight needs to take to get from starting position to ending position.

# start_row, start_col, end_row and end_col are 0-indexed. 

# Example
# Input:
# rows = 5
# cols = 5
# start_row = 0
# start_col = 0
# end_row = 4
# end_col = 1

# Output: 3
# 3 moves to reach from (0, 0) to (4, 1):
# (0, 0) -> (1, 2) -> (3, 3) -> (4, 1). 

# Complete the function below.
from collections import deque
def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    # Write your code here.
    # All the directions a knight can move starting from a given vertex
    DIRECTIONS = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    def getNeighbors(r,c):
        # Returns the valid neighbord
        neighbors = []
        for dr, dc in DIRECTIONS:
            new_r, new_c = r+dr, c+dc
            # Check boundaries
            if 0 <= new_r < rows and 0 <= new_c < cols:
                neighbors.append((new_r, new_c))
        return neighbors
    
    start_cell = start_row, start_col
    # BFS queue    
    q = deque([(start_cell, 0)])
    visited = {start_cell}
    
    while q:
        # Current cell and distance from source
        cell, count = q.popleft()
        
        # Reached end, return distance
        if cell == (end_row, end_col):
            return count
        
        # Explore neighbors
        for neighbor in getNeighbors(*cell):
            if neighbor not in visited:
                visited.add(neighbor)
                q.append((neighbor, count + 1))
    return -1