class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap={}
        if len(s)!=len(t):
            return False
        for letter in s:
            if hashmap.get(letter)==None:
                hashmap[letter]=1
            else:
                hashmap[letter]+=1
        
        for letter in t:
            if hashmap.get(letter)==None or hashmap[letter]==0:
                return False
            else:
                hashmap[letter]-=1
        return True
