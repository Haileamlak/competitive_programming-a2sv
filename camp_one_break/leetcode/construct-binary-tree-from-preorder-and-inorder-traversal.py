# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def get_index_in_inorder(left, right, x):
            i = left
            while inorder[i] != x: 
                i += 1
            
            return i

        def build_tree(inorder_left, inorder_right, preorder_left, preorder_right):
            if preorder_left > preorder_right:
                return None
            
            root = TreeNode(preorder[preorder_left])

            index = get_index_in_inorder(inorder_left, inorder_right, preorder[preorder_left])

            length = index - inorder_left
            root.left = build_tree(inorder_left, index - 1, preorder_left + 1, preorder_left + length)
            root.right = build_tree(index + 1, inorder_right, preorder_left + length + 1, preorder_right)

            return root
        
        return build_tree(0, len(inorder) - 1, 0, len(preorder) - 1)