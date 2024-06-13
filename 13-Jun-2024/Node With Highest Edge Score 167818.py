# Problem: Node With Highest Edge Score - https://leetcode.com/problems/node-with-highest-edge-score/description/

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        score = [0] * n

        for u, v in enumerate(edges):
            score[v] += u
        
        res = (0, score[0])
        for i, node_score in enumerate(score):
            if node_score > res[1]:
                res = (i, node_score)
        
        return res[0]