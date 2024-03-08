# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        curr_sum = 0

        def inverted_inorder(root):
            nonlocal curr_sum
            if not root:
                return 
            
            inverted_inorder(root.right)
            
            curr_sum += root.val
            root.val = curr_sum

            inverted_inorder(root.left)

        inverted_inorder(root)

        return root
