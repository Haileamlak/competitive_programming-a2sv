# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res = 0

        def traverse(root):
            nonlocal res
            if not root.left and not root.right:
                res = max(root.val, res)
                return (True, root.val, root.val, root.val) # (isBST, min, max, sum)
            
            if not root.left:
                right = traverse(root.right)

                curr = root.val + right[3]

                if right[0] and (root.val < right[1]):
                    res = max(res, curr)
                    return (True, min( right[1], root.val), max( right[2], root.val), curr)
            
                return (False, min( right[1], root.val), max( right[2], root.val), curr)
            
            if not root.right:
                left = traverse(root.left)

                curr = root.val + left[3]

                if left[0] and (root.val > left[2]):
                    res = max(res, curr)
                    return (True, min( left[1], root.val), max( left[2], root.val), curr)
            
                return (False, min( left[1], root.val), max( left[2], root.val), curr)
                



            left = traverse(root.left)
            right = traverse(root.right)

            curr = root.val + left[3] + right[3]
            if left[0] and right[0] and (left[2] < root.val < right[1]):
                res = max(res, curr)
                return (True, min([left[1], right[1], root.val]), max([left[2], right[2], root.val]), curr)
            
            return (False, min([left[1], right[1], root.val]), max([left[2], right[2], root.val]), curr)

        traverse(root)

        return res