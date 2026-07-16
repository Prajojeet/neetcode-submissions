class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        dic_s =dict()
        dic_t =dict()

        # In order of n sab kuch linear hi hoga!
        for n in s: 
            if dic_s.get(n)==None:
                dic_s[n]=1
            else:
                dic_s[n]+=1

        for n in t: 
            if dic_t.get(n)==None:
                dic_t[n]=1
            else:
                dic_t[n]+=1

        for key in dic_s:
            if dic_t.get(key)==None or dic_s[key]!=dic_t[key]: 
                return False

        return True

        