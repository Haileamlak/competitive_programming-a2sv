# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, preorderList):
        if not node:
            return

        preorderList.append(node.val)

        self.traverse(node.left, preorderList)
        self.traverse(node.right, preorderList)
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return

        preorderList = []
        self.traverse(root, preorderList)

        return preorderList
        
