class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        ln = 100000
        summ = 0
        flag = False
        while(r < len(nums)):
            summ += nums[r]
            if summ >= target:
                flag = True
                while(summ >= target and l <= r):
                    summ -= nums[l]
                    ln = min(ln, (r - l + 1))
                    l += 1
            r += 1
        
        return ln if flag == True else 0