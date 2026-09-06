class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for size in asteroids:
            # Base Case (with continue so that two times it doesn't run)
            if not stack:
                stack.append(size)
                continue
            # Normal case
            if size < 0:
                # Both incoming and existing are negative
                if stack[-1] < 0:
                    stack.append(size)
                # Incoming is bigger
                elif stack[-1] + size<0:
                    while(len(stack)>0 and stack[-1]>0 and stack[-1]+size<0):
                        stack.pop()
                    if not stack or stack[-1]<0:
                        stack.append(size)
                    elif stack[-1]+size==0:
                        stack.pop()
                    
                # Existing is equal and nothing if chota
                elif stack[-1] == abs(size):
                    stack.pop()

            else:
                stack.append(size)
                
        return stack
                