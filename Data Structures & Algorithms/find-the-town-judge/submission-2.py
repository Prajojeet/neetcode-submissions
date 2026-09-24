class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # A number with n - 1 incoming edges and 0 outgoing edges is a judge
        # [incoming, outgoing]
        network = {_:[0,0] for _ in range(1, n+1, 1)} 
        for pair in trust:
            network[pair[0]][1] += 1
            network[pair[1]][0] += 1
        
        for people in network:
            if network[people][0] == n - 1 and network[people][1] == 0:
                return people
        return -1

        

        