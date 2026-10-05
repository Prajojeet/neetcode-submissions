class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adjacency[crs].append(pre)

        print(adjacency)
        visited = set()
        cycle = set()
        stack = []

        def dfs(crs):
            # Base Case
            if crs in cycle:
                return False

            if crs in visited:
                return True

            cycle.add(crs)
            for pre in adjacency[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            stack.append(crs)
            visited.add(crs)
            return True
            

        for crs in adjacency:
            if not dfs(crs):
                print(crs)
                return []

        return stack # Reverse order, cause we want independent first
        