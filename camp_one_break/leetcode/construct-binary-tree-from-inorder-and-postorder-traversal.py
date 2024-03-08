# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def get_index_in_inorder(start, end, target):
            i = start
            while inorder[i] != target:
                i += 1
            
            return i

        def build_tree(in_left, in_right, post_left, post_right):
            if post_left > post_right:
                return None

            root = TreeNode(postorder[post_right])

            index = get_index_in_inorder(in_left, in_right, postorder[post_right])

            left_length = index - in_left

            root.left = build_tree(in_left, index - 1, post_left,  post_left + left_length - 1)
            root.right = build_tree(index + 1, in_right, post_left + left_length, post_right - 1)

            return root
        
        return build_tree(0, len(inorder) - 1, 0, len(postorder) - 1)