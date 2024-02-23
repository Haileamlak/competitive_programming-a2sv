# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        elements = []
        def traverseInorder(root):
            if not root:
                return
            
            traverseInorder(root.left)
            elements.append(root.val)
            traverseInorder(root.right)
        
        traverseInorder(root)

        modes = []
        mode = 0
        count = 1
        for i in range(1, len(elements)):
            if elements[i] == elements[i - 1]:
                count += 1
            else:
                if count > mode:
                    modes = [elements[i - 1]]
                    mode = count
                elif count == mode:
                    modes.append(elements[i - 1])

                count = 1

        if count > mode:
            modes = [elements[-1]]
        elif count == mode:
            modes.append(elements[-1])
        
        return modes