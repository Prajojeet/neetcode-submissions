class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        prefix, res = 0, 0
        for num in nums:
            prefix += num
            if (prefix - k) in hashmap:
                res += hashmap[prefix - k]
            
            if prefix not in hashmap:
                hashmap[prefix] = 1
            else:
                hashmap[prefix] += 1

        return res

