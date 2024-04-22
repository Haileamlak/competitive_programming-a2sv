# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        course_schedule = [[] for _ in range(numCourses)]
        indegree = defaultdict(int)

        for course_a, course_b in prerequisites:
            course_schedule[course_a].append(course_b)
            indegree[course_b] += 1
        
        ancestors = [set() for _ in range(numCourses)]

        queue = deque([course for course in range(numCourses) if course not in indegree])

        while queue:
            curr_course = queue.popleft()

            for next_course in course_schedule[curr_course]:
                indegree[next_course] -= 1
                ancestors[next_course] = ancestors[next_course].union(ancestors[curr_course])
                ancestors[next_course].add(curr_course)

                if indegree[next_course] == 0:
                    queue.append(next_course)

        res = []
        for u, v in queries:
            res.append(u in ancestors[v])
        
        return res