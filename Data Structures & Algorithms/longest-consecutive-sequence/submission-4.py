class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cou = set()
        for num in nums:
            cou.add(num)
        lon = 0
        for i in range(len(nums)):
            if (nums[i] - 1) not in cou:
                prev = nums[i]
                temp = 0
                while(prev in cou):
                    temp += 1
                    prev += 1
                lon = max(lon, temp)
        return lon
