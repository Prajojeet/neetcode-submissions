class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        res = 0
        for i in nums:
            prev = i - 1
            if prev not in unique:
                temp = 0
                curr  = prev + 1
                while(curr in unique):
                    temp += 1
                    curr += 1
                res = max(res, temp)
        return res