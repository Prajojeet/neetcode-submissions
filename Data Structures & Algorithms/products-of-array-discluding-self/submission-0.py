class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        for i in range(len(nums)):
            if nums[i]==0: # The case of Zero
                j=0
                product=1
                while(j<len(nums)): 
                    if j==i:
                        j+=1
                        continue
                    else:
                        product=product*nums[j]
                        j+=1 
                new=[0]*len(nums)
                new[i]=product
                return new
            
            else:
                product=product*nums[i]
        
        nums=[int((lambda x:product/x)(x)) for x in nums]
        return nums
