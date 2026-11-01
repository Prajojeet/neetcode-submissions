class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency = {i:[] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            adjacency[course].append(prerequisite)

        visited = set()
        def dfs(course):
            if course in visited: return False
            if not adjacency[course]: return True

            visited.add(course)
            for i in adjacency[course]:
                if not dfs(i): return False

            visited.remove(course)
            adjacency[course] = []
            return True

        for course in adjacency:
            if not dfs(course): return False
        return True