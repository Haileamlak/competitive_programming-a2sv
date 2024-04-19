# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        
        color = [0] * numCourses

        res = []
        def dfs(curr_course):
            if color[curr_course] == 1:
                return False

            color[curr_course] = 1
            for next_course in graph[curr_course]:
                if color[next_course] != 2 and not dfs(next_course):
                    return False

            color[curr_course] = 2
            res.append(curr_course)
            
            return True

        for node in range(numCourses):
            if not color[node] and not dfs(node):
                return []
        
        return res