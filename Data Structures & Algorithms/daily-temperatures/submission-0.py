class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Define a monotonic decreasing array situation
        # Store a tuple (index, temp) inside the stack 
        stack=[]
        ans=[0]*len(temperatures)
        for index, temperature in enumerate(temperatures):
            # Empty stack
            if not stack:
                stack.append((index,temperature))
            else:
                # Add if decreasing
                if stack[-1][1]>=temperature:
                    stack.append((index,temperature))
                else:
                    # Remove in a loop
                    while(len(stack)>0 and stack[-1][1]<temperature):
                        ans[stack[-1][0]]=index-stack[-1][0]
                        stack.pop()
                    stack.append((index,temperature))
        return ans