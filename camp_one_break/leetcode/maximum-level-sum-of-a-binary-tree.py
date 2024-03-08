# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        curr_sum = 0
        maximum = (float('-inf'), 0)

        queue = deque([root, None])
        level = 1
        while queue:
            curr = queue.popleft()
            if not curr:
                if curr_sum > maximum[0]:
                    maximum = (curr_sum, level)

                curr_sum = 0
                level += 1

                if queue:
                    queue.append(None)
            else:
                curr_sum += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        
        return maximum[1]