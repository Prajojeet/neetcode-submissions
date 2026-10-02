class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency = {i:[] for i in range(numCourses)}
        for course, requirement in prerequisites:
            adjacency[course].append(requirement)  
        
        # Finding cycles
        visited = set()
        def dfs(course):
            # Base Case - for Loop detection
            if course in visited:
                return False

            # Base Case - No pre requisites
            if adjacency[course] == []:
                return True

            visited.add(course)
            for requirement in adjacency[course]:
                if not dfs(requirement): return False
            
            # Clear the list and remove the course from visited
            visited.remove(course)
            adjacency[course] = []
            return True

        # Looping through all because there can be disconnected nodes in the graph
        for course in range(numCourses):
            if not dfs(course): return False
        
        return True
