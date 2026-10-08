class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        stack = [] # Need to store a tuple to store the index as well

        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp, i))
                continue
            
            if stack[-1][0] < temp:
                while(stack and stack[-1][0] < temp):
                    res[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
            stack.append((temp, i))

        return res