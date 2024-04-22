# Problem: Parallel Courses III - https://leetcode.com/problems/parallel-courses-iii/

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]
        indegree = [0 for _ in range(n)]

        for prev_course, next_course in relations:
            graph[prev_course - 1].append(next_course - 1)
            indegree[next_course - 1] += 1
        
        answer = time.copy()

        queue = deque([course for course in range(n) if not indegree[course]])

        while queue:
            curr_course = queue.popleft()
            
            for next_course in graph[curr_course]:
                indegree[next_course] -= 1
                answer[next_course] = max(answer[next_course], time[next_course] + answer[curr_course])

                if indegree[next_course] == 0:
                    queue.append(next_course)
        

        return max(answer)