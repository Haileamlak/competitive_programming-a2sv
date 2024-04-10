# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def graph(self, root):
        adj_list = defaultdict(list)

        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if curr.left:
                adj_list[curr.val].append(curr.left.val)
                adj_list[curr.left.val].append(curr.val)
                queue.append(curr.left)
                
            if curr.right:
                adj_list[curr.val].append(curr.right.val)
                adj_list[curr.right.val].append(curr.val)
                queue.append(curr.right)

        return adj_list

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj_list = self.graph(root)

        queue = deque([target.val])
        visited = set([target.val])
        level = 0
        while queue:
            if level == k:
                return list(queue)
            
            for i in range(len(queue)):
                curr = queue.popleft()
                for node in adj_list[curr]:
                    if node not in visited:
                        visited.add(node)
                        queue.append(node)

            level += 1
        
        return []