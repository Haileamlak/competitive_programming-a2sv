# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findInorderPredecessor(self, node):
        curr = node
        while curr.right:
            curr = curr.right
        
        return curr

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        modes = []
        max_streak = 0
        count = 0
        curr_num = 0

        curr = root
        while curr:
            if curr.left:
                friend = self.findInorderPredecessor(curr.left)
                friend.right = curr

                temp = curr.left
                curr.left = None
                curr = temp
            
            else:
                if curr.val == curr_num:
                    count += 1
                else:
                    count = 1
                    curr_num = curr.val
                
                if count > max_streak:
                    modes = [curr.val]
                    max_streak = count
                elif count == max_streak:
                    modes.append(curr.val)

                curr = curr.right

        return modes
