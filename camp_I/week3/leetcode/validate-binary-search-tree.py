# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        def traverse(node):
            if not node:
                return
            # traverse the left subtree inorder
            traverse(node.left)

            # append the current node
            answer.append(node.val)

            # traverse the right subtree inorder
            traverse(node.right)
        
        traverse(root)

        return answer

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodes = self.inorderTraversal(root)

        for i in range(1, len(nodes)):
            if nodes[i] <= nodes[i - 1]:
                return False
        
        return True