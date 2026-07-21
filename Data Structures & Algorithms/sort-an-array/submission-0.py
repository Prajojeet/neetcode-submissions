class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Selection sort method (Find the minimum and place it in the front)
        # How to store the index of the minimum number was also a learning using this method
        # Basically, we will swap the smallest index with the loop circle we are currently in at that point of time
        n = len(nums)
        for i in range(n):
            min=nums[i]
            ind=i
            for j in range(i+1,n):
                if nums[j]<min:
                    min=nums[j]
                    ind=j
            temp=nums[i]
            nums[i]=min
            nums[ind]=temp 
        return nums