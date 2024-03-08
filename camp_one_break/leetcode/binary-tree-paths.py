# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        path = []
        def depth_first_traverse(root):
            if not root:
                return
                
            if not root.left and not root.right:
                path.append(str(root.val))
                res.append(''.join(path))
                path.pop()
            
            path.append(str(root.val) + '->')
            depth_first_traverse(root.left)
            depth_first_traverse(root.right)
            path.pop()
        
        depth_first_traverse(root)
        return res