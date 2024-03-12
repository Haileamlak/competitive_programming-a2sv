# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def height(root):
            res = 0
            while root:
                root = root.left
                res += 1

            return res

        def full(root, h):
            right_node = root
            while right_node:
                right_node = right_node.right
                h -= 1

            return not h
        
        def binary_search_dfs(root, row, col, h):
            if not root:
                return (pow(2, row ) - 1) + (col - pow(2, row))

            left_is_full = full(root.left, h - 1)
            right_is_full = full(root.right, h - 1)

            if (left_is_full and right_is_full) or (not left_is_full and not right_is_full) or right_is_full:
                return binary_search_dfs(root.left, row + 1, 2 * col, h - 1)
            
            
            return binary_search_dfs(root.right, row + 1, 2 * col + 1, h - 1)
        
        h = height(root)
        return binary_search_dfs(root, 0, 1, h)