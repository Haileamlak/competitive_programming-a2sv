# Problem: Cousins in Binary Tree II - https://leetcode.com/problems/cousins-in-binary-tree-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        level_sum = []
        sibling_sum = {None: root.val}
        while queue:
            curr_sum = 0
            for _ in range(len(queue)):
                curr_node = queue.popleft()
                curr_sum += curr_node.val

                my_sibling_sum = 0
                if curr_node.left:
                    queue.append(curr_node.left)
                    my_sibling_sum += curr_node.left.val
                    
                if curr_node.right:
                    queue.append(curr_node.right)
                    my_sibling_sum += curr_node.right.val

                sibling_sum[curr_node] = my_sibling_sum

            level_sum.append(curr_sum)

        queue = deque([(root, None)])
        i = 0
        while queue:
            curr_sum = level_sum[i]
            for _ in range(len(queue)):
                curr_node, parent = queue.popleft()

                curr_node.val = curr_sum - sibling_sum[parent]

                if curr_node.left:
                    queue.append((curr_node.left, curr_node))
            
                if curr_node.right:
                    queue.append((curr_node.right, curr_node))

            i += 1

        return root