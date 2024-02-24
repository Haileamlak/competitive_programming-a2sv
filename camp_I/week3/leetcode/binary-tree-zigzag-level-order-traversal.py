# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        elements = defaultdict(list)
        def traverse(root, row):
            if not root:
                return
            
            traverse(root.left, row + 1)
            elements[row] += [root.val]
            traverse(root.right, row + 1)
        
        traverse(root, 0)
        result = []
        for row, elems in sorted(elements.items()):
            if row % 2:
                elems.reverse()
            result.append(elems)
        
        return result
        