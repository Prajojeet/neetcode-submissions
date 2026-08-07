class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sorting itself takes minimum nlogn, but we want the answer to be in n only

        counter=set(nums)
        maxima=0
        for i in nums:
            temp=0
            prev=i-1
            curr=i
            if prev not in counter:
                while (curr in counter):
                    temp+=1
                    curr+=1
                maxima=max(temp,maxima)
        return maxima


        
        