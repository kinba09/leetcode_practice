"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        
        old_to_new: dict[node,node] = {}
        def dfs(orig: 'Node') -> 'Node':
            if orig in old_to_new:
                return old_to_new[orig]
            
            copy = Node(orig.val)
            old_to_new[orig] = copy

            for nei in orig.neighbors:
                copy.neighbors.append(dfs(nei)) 
            return copy
        return dfs(node)
