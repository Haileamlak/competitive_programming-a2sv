# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = [[] for _ in range(n)]

        # representing the tree using adjacency list
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        def bfs(node, father):
            visited = [False] * n
            visited[node] = True

            queue = deque([node])

            while queue:
                ans = []
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    
                    for neighbour in tree[curr]:
                        if not visited[neighbour]:
                            visited[neighbour] = True
                            father[neighbour] = curr
                            queue.append(neighbour)

            return curr
        
        # one end of the one of longest paths of the tree
        start_node = bfs(0, {})

        # the other end of the longest path
        father = {}
        end_node = bfs(start_node, father)
        
        # collecting the nodes in the longest path
        longest = [end_node]
        curr = end_node
        while curr in father:
            curr = father[curr]
            longest.append(curr)
        

        # the answer will be the middle element in the longest path if it's length is odd. 
        # Other wise if it's length is even the answer will be the two middle nodes.
        
        n = len(longest)
        middle = (n - 1) // 2
        end = (n // 2) + 1
        return longest[middle: end]