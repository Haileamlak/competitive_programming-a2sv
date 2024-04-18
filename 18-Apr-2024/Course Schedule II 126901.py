# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        graph = defaultdict(list)
        for u, v in prerequisites:
            indegree[u] += 1
            graph[v].append(u)
        
        queue = deque()
        visited = [False] * numCourses
        for node in range(numCourses):
            if node not in indegree:
                queue.append(node)
                visited[node] = True
        
        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr)

            for course in graph[curr]:
                if not visited[course]:
                    indegree[course] -= 1

                    if indegree[course] == 0:
                        queue.append(course)
                        visited[course] = True
        
        return res if len(res) == numCourses else []