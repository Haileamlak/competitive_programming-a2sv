# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        arr = []
        def preorder(root):
            if not root.left and not root.right:
                return (root, root)
            
            if not root.left:
                right = preorder(root.right)
                return (root, right[1])
            
            if not root.right:
                left = preorder(root.left)
                root.right = root.left
                root.left = None
                return (root, left[1])
            
            left = preorder(root.left)
            right = preorder(root.right)

            root.right = root.left
            root.left = None
            left[1].right = right[0]
            return (root, right[1])

        preorder(root)