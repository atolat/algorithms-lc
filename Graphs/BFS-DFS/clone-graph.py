# 133. Clone Graph
# Medium

# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.

# Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }

# Time Complexity: O(V+E) - Number of vertices + edges
# Space Complexity
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

# BFS

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        # Map to hold clone nodes
        # As every node is visited, add a deep copy of the node to clone
        clone = collections.defaultdict(lambda: Node)

        # Initialize a BFS queue
        q = collections.deque([node])
        clone[node] = Node(node.val, [])

        while q:
            # Pop node from queue and mark it as visited
            current_node = q.popleft()

            # Explore the neighbors
            for neighbor in current_node.neighbors:
                if neighbor not in clone:
                    # Create a new node corresponding to every node
                    clone[neighbor] = Node(neighbor.val, [])
                    q.append(neighbor)
                # Append the neighbors
                clone[current_node].neighbors.append(clone[neighbor])
        return clone[node]

# DFS

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        # Map to hold clone nodes
        # As every node is visited, add a deep copy of the node to clone
        clone = collections.defaultdict(lambda: Node)

        def dfs(node):
            # Base Case
            # If node is already cloned, return clone
            if node in clone:
                return clone[node]

            # Logic
            # Create a clone of current node
            clone[node] = Node(node.val, [])

            # Recursively create clones of neighbors and add them to node's neighbor list
            for neighbor in node.neighbors:
                clone[node].neighbors.append(dfs(neighbor))
            return clone[node]

        return dfs(node)
