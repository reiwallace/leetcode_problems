from typing import Optional
from utils.node import Node

class Solution:
    def __init__(self):
        self.registery = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None: return None
        new = Node(node.val, [])
        self.registery[new.val] = new
        for neighbor in node.neighbors:
            if neighbor.val not in self.registery:
                new.neighbors.append(self.cloneGraph(neighbor))
            else:
                new.neighbors.append(self.registery[neighbor.val])
        return new
