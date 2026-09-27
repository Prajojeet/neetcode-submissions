class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Unique = set(nums)
        result = 0
        for i in nums:
            prev = i - 1
            curr = i
            temp = 0
            if prev not in Unique:
                while curr in Unique:
                    temp += 1
                    curr += 1

            result = max(result, temp)

        return result
            