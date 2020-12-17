# 733. Flood Fill
# Easy

# 1598

# 220

# Add to List

# Share
# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

# At the end, return the modified image.

# Example 1:
# Input:
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation:
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.
# Time Complexity: O(m*n) -> size of grid
# Space Complexity: O(m*n)
# Approach:
# Use BFS or DFS to explore all neighbors of the starting node. If the color is oldColor, change it to newColor
# More comments on both approaches in-line...
# DFS
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        # Edge Case
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image

        # Get neighboring cells
        def getNeighbors(r, c, ROW, COLUMN):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < ROW and 0 <= nc < COLUMN:
                    yield nr, nc
        # Using DFS
        ROW = len(image)
        COLUMN = len(image[0])

        def dfs(sr, sc):
            image[sr][sc] = newColor
            for nr, nc in getNeighbors(sr, sc, ROW, COLUMN):
                if image[nr][nc] == oldColor:
                    dfs(nr, nc)

        dfs(sr, sc)
        return image

# BFS
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        # Edge Case
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image

        # Get neighboring cells
        def getNeighbors(r, c, ROW, COLUMN):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < ROW and 0 <= nc < COLUMN:
                    yield nr, nc

        # Initialize queue for bfs
        ROW = len(image)
        COLUMN = len(image[0])
        q = collections.deque()
        image[sr][sc] = newColor
        q.append((sr, sc))

        while q:
            r, c = q.popleft()
            for nr, nc in getNeighbors(r, c, ROW, COLUMN):
                if image[nr][nc] == oldColor:
                    image[nr][nc] = newColor
                    q.append((nr, nc))
        return image
