# Problem: Maximum Depth of N-ary Tree - https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
            
        def max_depth(curr_node):
            if not curr_node.children:
                return 1

            return 1 + max(max_depth(node) for node in curr_node.children)
        
        return max_depth(root)