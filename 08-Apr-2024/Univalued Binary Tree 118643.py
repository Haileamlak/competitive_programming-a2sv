# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        
        while queue:
            curr = queue.popleft()
            if curr.left:
                if curr.left.val != curr.val:
                    return False
                
                queue.append(curr.left)

            if curr.right:
                if curr.right.val != curr.val:
                    return False
                
                queue.append(curr.right)

        return True