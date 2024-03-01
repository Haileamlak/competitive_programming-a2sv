# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        def traverse(root):
            if not root:
                return
            
            traverse(root.left)
            nodes.append(root.val)
            traverse(root.right)
        
        traverse(root)

        def getBinarySearchTree(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            root = TreeNode(nodes[mid])
            root.left = getBinarySearchTree(left, mid - 1)
            root.right = getBinarySearchTree(mid + 1, right)
            return root

        return getBinarySearchTree(0, len(nodes) - 1)