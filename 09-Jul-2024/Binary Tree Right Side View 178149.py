# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        queue = deque([root])
        res = []
        while queue:
            res.append(queue[-1].val)
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)
        
        return res