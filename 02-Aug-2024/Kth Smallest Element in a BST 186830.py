# Problem: Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        res = 0

        def getKthSmallest(root):
            nonlocal count, res
            
            if not root:
                return

            getKthSmallest(root.left)

            count += 1
            
            if count == k:
                res = root.val
                
            if count < k:
                getKthSmallest(root.right)

        getKthSmallest(root)
        return res