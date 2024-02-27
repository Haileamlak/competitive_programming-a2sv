# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        elements = defaultdict(lambda: defaultdict(list))

        def traverse(root, row, col):
            if not root:
                return
            
            elements[col][row] += [root.val]
            traverse(root.left, row + 1, col - 1)
            traverse(root.right, row + 1, col + 1)
        
        traverse(root, 0, 0)

        answer = []
        for col, cols in sorted(elements.items()):
            arr = []
            for row, nums in sorted(cols.items()):
                nums.sort()
                arr += nums
            answer.append(arr)
        
        return answer