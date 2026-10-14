class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1} # store summ:count; 0:1 suggests that if any element equals k, then 1 added
        summ, res = 0, 0
        for i in range(len(nums)):
            summ += nums[i]
            if (summ - k) in prefix:
                res += prefix[summ - k]

            if summ not in prefix:
                prefix[summ] = 1
            else:
                prefix[summ] += 1

        return res

                
