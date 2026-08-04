class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        counter1={}
        counter2={}

        for letter in s:
            if letter not in counter1:
                counter1[letter]=1
            else:
                counter1[letter]+=1
        
        for letter in t:
            if letter not in counter2:
                counter2[letter]=1
            else:
                counter2[letter]+=1
        
        return counter1==counter2