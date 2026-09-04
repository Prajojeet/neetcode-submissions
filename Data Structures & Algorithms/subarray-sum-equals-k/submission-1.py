class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix={0:1} # Base case ie if first elements sums to one
        curr_sum=0
        ans=0
        for num in nums:
            curr_sum+=num
            if (curr_sum-k) in prefix:
                ans+=prefix[curr_sum-k]
            
            if curr_sum not in prefix:
                prefix[curr_sum]=1
            else:
                prefix[curr_sum]+=1
        
        return ans