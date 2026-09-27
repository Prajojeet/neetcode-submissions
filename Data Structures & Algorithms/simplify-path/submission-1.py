class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        word = ''
        for char in path + '/':
            if char == '/':
                if word == '..':
                    if stack: stack.pop()
                elif word == '' or word == '.':
                    word = ''
                    continue
                else:
                    stack.append(word)
                
                word = ''
                
            else:
                word += char

        return '/' + '/'.join(stack)
