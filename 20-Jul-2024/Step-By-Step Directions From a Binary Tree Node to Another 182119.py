# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        path1 = []
        path2 = []

        def dfs(node, path):
            nonlocal path1, path2
            if not node:
                return 
            
            if node.val == startValue:
                path1 = path.copy()

            elif node.val == destValue:
                path2 = path.copy()
            
            path.append('L')
            dfs(node.left, path)
            path.pop()
            path.append('R')
            dfs(node.right, path)
            path.pop()
        
        dfs(root, [])

        i = 0
        while i < len(path1) and i < len(path2) and path1[i] == path2[i]:
            i += 1

        return 'U' * (len(path1) - i) + ''.join(path2[i:])