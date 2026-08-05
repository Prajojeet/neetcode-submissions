class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Need to handle both separately finding the lower bound and then the two pointer
        left,l=0,0
        right=len(numbers)-1
        while(left<right):
            if numbers[left]+numbers[right]==target:
                return [left+1,right+1]
            elif numbers[left]+numbers[right]<target:
                left+=1
            else:
                right-=1