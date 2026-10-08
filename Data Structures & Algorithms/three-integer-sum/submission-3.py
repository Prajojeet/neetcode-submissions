class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Pick a element and two sum on other
        res = []

        # sort
        nums.sort()
        visited = set()

        # twosum
        def twosum(index, target):
            l = index
            r = len(nums) - 1

            while(r > l):
                if target == nums[r] + nums[l]:
                    res.append([-target, nums[r], nums[l]])
                    l += 1
                    while(nums[l - 1] == nums[l] and l < r):
                        l += 1
                elif target < nums[r] + nums[l]:
                    r -= 1
                else:
                    l += 1 


        for i in range(len(nums)):
            if nums[i] not in visited:
                visited.add(nums[i])
                twosum(i + 1, -nums[i])
            else:
                continue

        return res
