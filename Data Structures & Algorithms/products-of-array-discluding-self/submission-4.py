class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1]*l

        pro = 1
        for i in range(l - 1):
            pro = pro * nums[i]
            res[i + 1] = pro

        temp = 1
        for i in range(l - 1, 0, -1):
            temp = temp * nums[i]
            res[i - 1] = res[i - 1] * temp

        return res