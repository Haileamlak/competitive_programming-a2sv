# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root
        previous = None

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            while not curr and stack:
                curr = stack[-1]
                if curr.right == None or curr.right == previous:
                    res.append(curr.val)
                    previous = curr
                    curr = None
                    stack.pop()
                    
                else:
                    curr = curr.right

        return res