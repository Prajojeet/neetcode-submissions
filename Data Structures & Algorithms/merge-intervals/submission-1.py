class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() # Sorts based on first element
        n = len(intervals)
        l = intervals[0][0]
        r = intervals[0][1]
        ans = []

        # Base Case
        if n == 1:
            return intervals

        for i in range(1, n):
            if intervals[i][0] <= r:
                r = max(r, intervals[i][1])
            else:
                ans.append([l, r])
                l = intervals[i][0]
                r = intervals[i][1]

        ans.append([l, r])
        return ans