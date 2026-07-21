class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Let me make a hash map of thing target-nums[i]; I can basically store things in a dictionary
        dic={}
        for i in range(len(nums)):
            if dic.get(target-nums[i])==None:
                dic[target-nums[i]]=1
            else:
                dic[target-nums[i]]+=1
        # If some things are same, isn't possible because elements in the list cannot repeat
        output=[]
        for i in range(len(nums)):
            if nums[i] == target-nums[i]:
                if dic.get(nums[i])==2:
                    output.append(i)
            elif dic.get(nums[i])==1:
                output.append(i)

        return output

