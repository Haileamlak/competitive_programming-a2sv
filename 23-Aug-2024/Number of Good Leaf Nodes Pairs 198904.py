# Problem: Number of Good Leaf Nodes Pairs - https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        graph = defaultdict(list)
        leaf_nodes = []

        def dfs(node):
            if not node.left and not node.right:
                leaf_nodes.append(node)
                return

            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                dfs(node.left)

            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                dfs(node.right)

        dfs(root)    

        def reachable(node):
            res = 0
            queue = deque([(node, node)])
            i = 0
            while i <= distance and queue:
                for _ in range(len(queue)):
                    curr, parent = queue.popleft()
                    if not curr.left and not curr.right:
                        res += 1
                        print(node.val, curr.val)
                    for adj in graph[curr]:
                        if adj != parent:
                            queue.append((adj, curr))

                i += 1

            return res

        res = 0
        for node in leaf_nodes:
            res += reachable(node)  

        return (res - len(leaf_nodes)) // 2