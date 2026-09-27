class Solution:
    def decodeString(self, s: str) -> str:
         
        stack = []
        for char in s:
            if char == ']':
                Bword = ''
                while(stack[-1] != '['):
                    Bword = stack.pop() + Bword
                stack.pop() # Removes the bracket '['

                # The integer
                k = ''
                while stack and stack[-1].isnumeric():
                    k = stack.pop() + k

                # Finally add the modified version to the stack
                stack.append(int(k) * Bword)

            else:
                stack.append(char)

        return ''.join(stack)