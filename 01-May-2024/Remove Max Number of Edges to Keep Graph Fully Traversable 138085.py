# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice_parent = [i for i in range(n)]
        alice_size = [0 for _ in range(n)]

        bob_parent = [i for i in range(n)]
        bob_size = [0 for _ in range(n)]

        def get(x, parent):
            root = x
            while root != parent[root]:
                root = parent[root]
            
            while x != parent[x]:
                x, parent[x] = parent[x], root
            
            return x
        
        def union(x, y, parent, size):
            px, py = get(x, parent), get(y, parent)

            if px != py:
                if size[px] > size[py]:
                    px, py = py, px
                
                parent[px] = py
                size[py] += size[px]
            
        res = 0
        for _type, u, v in edges:
            u -= 1
            v -= 1

            if _type == 3:
                if get(u, alice_parent) != get(v, alice_parent) or get(u, bob_parent) != get(v, bob_parent):
                    union(u, v, alice_parent, alice_size)
                    union(u, v, bob_parent, bob_size)
                else:
                    res += 1

        for _type, u, v in edges:
            u -= 1
            v -= 1

            if _type == 1:
                if get(u, alice_parent) != get(v, alice_parent):
                    union(u, v, alice_parent, alice_size)
                else:
                    res += 1

            elif _type == 2:
                if get(u, bob_parent) != get(v, bob_parent):
                    union(u, v, bob_parent, bob_size)
                else:
                    res += 1
        
        flag = False
        for i, p in enumerate(alice_parent):
            if i == p:
                if flag:
                    return -1
                flag = True

        flag = False
        for i, p in enumerate(bob_parent):
            if i == p:
                if flag:
                    return -1
                flag = True
            
        return res