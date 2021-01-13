# 1041. Robot Bounded In Circle
# Medium

# On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degrees to the right.
# The robot performs the instructions given in order, and repeats them forever.

# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

# Example 1:

# Input: instructions = "GGLLGG"
# Output: true
# Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
# When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
# Example 2:

# Input: instructions = "GG"
# Output: false
# Explanation: The robot moves north indefinitely.
# Example 3:

# Input: instructions = "GL"
# Output: true
# Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...

# TIME COMPLEXITY: O(N)
# SPACE COMPLEXITY: O(1)
class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        # Indexes of dirs represent directions - 0:North, 1:East, 2:South, 3:West
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        # Initially we start at origin
        x, y = 0, 0
        # Start facing 0:North
        direction_facing = 0

        for instruction in instructions:
            # If the next instruction is "L", robot faces 90 degrees left
            # Initial -> +90 degrees left
            # 0:North -> 3:West
            # 1:East -> 0:North
            # 2:South -> 1:East
            # 3:West -> 2:South
            if instruction == 'L':
                direction_facing = (direction_facing + 3) % 4
            # Similarly if next instruction is "R", robot faces 90 degrees right
            # Initial -> +90 degrees right
            # 0:North -> 1:East
            # 1:East -> 2:South
            # 2:South -> 3:West
            # 3:West -> 0:North
            elif instruction == 'R':
                direction_facing = (direction_facing + 1) % 4
            # If next instruction is "G"
            # Robot walks straight in the direction it is facing
            else:
                x += dirs[direction_facing][0]
                y += dirs[direction_facing][1]

        # Finally, if robot is back at origin or facing any direction other than 0:North, it will be bound in a circle
        return (x == 0 and y == 0) or direction_facing != 0
