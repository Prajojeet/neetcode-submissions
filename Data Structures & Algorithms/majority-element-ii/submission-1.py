class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        limiter=len(nums)//3
        freq={}
        ans=set()
        for num in nums:
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1
            
            if freq[num]>limiter:
                ans.add(num)
        return list(ans)
