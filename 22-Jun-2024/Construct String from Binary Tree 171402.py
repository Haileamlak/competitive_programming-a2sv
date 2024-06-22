# Problem: Construct String from Binary Tree - https://leetcode.com/problems/construct-string-from-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pre_order(self, root: TreeNode):
        res = '(' + str(root.val)

        if root.left and root.right:
            res += self.pre_order(root.left)
            res += self.pre_order(root.right)

        elif root.right:
            res += "()"
            res += self.pre_order(root.right)

        elif root.left:
            res += self.pre_order(root.left)

        res += ')'

        return res

    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
            
        res = self.pre_order(root)

        if res[0] == '(':
            return res[1:len(res) - 1]

        return res
        