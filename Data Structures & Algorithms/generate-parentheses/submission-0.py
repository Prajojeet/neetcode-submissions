class Solution:
    def __init__(self):
        self.ans=[]

    def bt_dfs(self, path, n, opening, closing):
        # Base Case 1
        if opening>n:
            return

        # Base Case 2
        if opening==n and closing==n:
            self.ans.append("".join(path[:]))
            return 

        # Loop for adding paranthesis
        # Constraint (The number of closed pararanthesis<number of open paranthesis)
        for parenthesis in ['(',')']:
            if parenthesis=='(':
                path.append(parenthesis)
                self.bt_dfs(path, n, opening+1 , closing)
                path.pop()
            elif parenthesis==')' and closing < opening:
                path.append(parenthesis)
                self.bt_dfs(path, n, opening, closing+1)
                path.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        self.bt_dfs([], n, 0, 0)
        return self.ans