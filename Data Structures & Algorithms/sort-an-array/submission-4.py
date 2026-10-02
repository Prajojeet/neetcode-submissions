class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # # Bubble Sort - check sorted or not, keep swapping the elements again and again once all are sortec!
        # condition = True
        # while(condition):
        #     condition = False
        #     for i in range(len(nums) - 1):
        #         if nums[i] > nums[i + 1]:
        #             condition = True
        #             temp = nums[i]
        #             nums[i] = nums[i + 1]
        #             nums[i + 1] = temp

        # return nums

        # Insertion Sort - take the element and keep it in its position, ie sort sublists

        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while(j >= 0 and nums[j] > key):
                nums[j + 1] = nums[j]
                j -= 1
            nums[j+1] = key


        return nums

