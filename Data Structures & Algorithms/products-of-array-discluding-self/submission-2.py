class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Product - from positive side and from negative side
        output = [1] * n

        l = 1
        for i in range(0, n - 1, 1):
            l = l * nums[i]
            output[i + 1] = l

        r = 1
        for i in range(n - 1, 0, -1):
            r = r * nums[i]
            output[i - 1] = output[i - 1] * r

        return output