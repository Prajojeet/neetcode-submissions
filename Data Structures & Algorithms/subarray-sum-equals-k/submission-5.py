class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1} # Store sum and count
        summ = 0
        res = 0
        for i in range(len(nums)):
            summ += nums[i]
            if (summ - k) in hashmap:
                res += hashmap[summ - k]

            if summ in hashmap:
                hashmap[summ] += 1
            else:
                hashmap[summ] = 1
        return res