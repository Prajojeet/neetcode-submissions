class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            temp = [0]*26
            for char in word:
                temp[ord(char) - ord('a')] += 1
            
            temp = tuple(temp)
            if temp in hashmap:
                hashmap[temp].append(word)
            else:
                hashmap[temp] = []
                hashmap[temp].append(word)

        res = []
        for value in hashmap.values():
            res.append(value)

        return res