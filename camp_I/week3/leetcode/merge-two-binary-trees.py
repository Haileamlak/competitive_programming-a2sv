# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        elif not root1:
            root2.right = self.mergeTrees(root2.right, None)
            root2.left = self.mergeTrees(root2.left, None)
            return root2
        elif not root2:
            root1.right = self.mergeTrees(root1.right, None)
            root1.left = self.mergeTrees(root1.left, None)
            return root1
        
        newNode = TreeNode(root1.val + root2.val)
        newNode.left = self.mergeTrees(root1.left, root2.left)
        newNode.right = self.mergeTrees(root1.right, root2.right)
        return newNode
        
        # return self.mergeTrees(root1, root2)
            