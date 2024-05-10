# Problem: House Robber III - https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def _rob(house, can_rob):
            if not house:
                return 0
            
            if can_rob:
                res1 = house.val + _rob(house.left, not can_rob) + _rob(house.right, not can_rob)
                res2 = _rob(house.left, can_rob) + _rob(house.right, can_rob)
                return max(res1, res2)
            else:
                return _rob(house.left, not can_rob) + _rob(house.right, not can_rob)

        return _rob(root, True)