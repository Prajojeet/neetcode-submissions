class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # We should aim for n2 time complexity meaning one element pakdo and bakio pe lagao and dictionary mai store karo and then last mai ek ek karke append karo

        hashmap={}
        output=[]
        for i in range(len(nums)-2):
            target=-nums[i]
            j=i+1
            counter={}
            while(j<len(nums)):
                if nums[j] not in counter:
                    counter[target-nums[j]]=j
                    j+=1
                else:
                    arr=[nums[i],nums[counter[nums[j]]],nums[j]]
                    arr.sort()
                    hashmap[tuple(arr)]=1
                    j+=1
        for keys in hashmap:
            output.append(list(keys))
        return output
