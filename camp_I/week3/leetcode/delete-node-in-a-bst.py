# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getInorderSuccessor(self, root):
        if not root.left:
            return root.val
              
        return self.getInorderSuccessor(root.left)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            if not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                root.val = self.getInorderSuccessor(root.right)

                root.right = self.deleteNode(root.right, root.val)
        
        return root