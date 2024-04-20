# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        rich_graph = [[] for _ in range(n)]
        richer_than = defaultdict(int)

        for a, b in richer:
            rich_graph[a].append(b)
            richer_than[b] += 1

        queue = deque()
        for person in range(n):
            if person not in richer_than:
                queue.append(person)

        answer = [person for person in range(n)]

        while queue:
            person = queue.popleft()
            for poorer in rich_graph[person]:
                if quiet[answer[person]] < quiet[answer[poorer]]:
                    answer[poorer] = answer[person]

                richer_than[poorer] -= 1
                if richer_than[poorer] == 0:
                    queue.append(poorer)

        return answer
