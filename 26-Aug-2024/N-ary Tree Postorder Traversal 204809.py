# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        def traverse(root, arr):
            if not root:
                return 
            
            for child in root.children:
                traverse(child, arr)
            
            arr.append(root.val)
        
        res = []
        traverse(root, res)

        return res