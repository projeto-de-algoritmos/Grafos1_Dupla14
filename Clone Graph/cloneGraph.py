class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node'):
        if not node:
            return None
        
        clone_map = {}
        visited = set()
        
        def clone(node):
            if node in clone_map:
                return clone_map[node]
            
            clone_node = Node(node.val)
            
            clone_map[node] = clone_node
            
            for neighbor in node.neighbors:
                clone_neighbor = clone(neighbor)
                clone_node.neighbors.append(clone_neighbor)
            
            return clone_node
        
        return clone(node)
