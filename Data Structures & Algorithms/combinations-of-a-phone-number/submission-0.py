class Solution:
    def __init__(self):
        self.ans=[]
        self.hashmap={2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'], 5:['j','k','l'], 6:['m','n','o'], 7:['p','q','r','s'], 8:['t','u','v'], 9:['w','x','y','z']}

    def bt_dfs(self, path, position, digits):
        # Base Case 1
        if len(path)==len(digits):
            self.ans.append("".join(path[:]))
            return

        for char in self.hashmap[int(digits[position])]:
            path.append(char)
            self.bt_dfs(path, position+1, digits)
            path.pop()
        
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.bt_dfs([],0,digits)
        return self.ans
