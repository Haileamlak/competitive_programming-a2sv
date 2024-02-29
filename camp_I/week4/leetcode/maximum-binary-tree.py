# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def indexOfMaximum(left, right):
            index = left
            i = left
            while i <= right:
                if nums[i] > nums[index]:
                    index = i

                i += 1
            
            return index    

        def getMaximumBinaryTree(left, right):
            if left > right:
                return None
            
            i = indexOfMaximum(left, right)

            root = TreeNode(nums[i])
            root.left = getMaximumBinaryTree(left, i - 1)
            root.right = getMaximumBinaryTree(i + 1, right)

            return root

        return getMaximumBinaryTree(0, len(nums) - 1)
    