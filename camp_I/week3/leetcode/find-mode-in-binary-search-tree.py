# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        modes = []
        max_streak = 0
        count = 0
        curr_num = 0
        
        def traverseInorder(root):
            nonlocal count, max_streak, curr_num, modes
            if not root:
                return
            
            traverseInorder(root.left)

            if root.val == curr_num:
                count += 1
            else:
                count = 1
                curr_num = root.val
            
            if count > max_streak:
                modes = [root.val]
                max_streak = count
            elif count == max_streak:
                modes.append(root.val)

            traverseInorder(root.right)
        
        traverseInorder(root)

        return modes