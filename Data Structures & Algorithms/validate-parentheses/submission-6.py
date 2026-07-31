class Solution:
    def isValid(self, s: str) -> bool:
        st=[]

        if len(s)%2!=0:
            return False
        
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="{" or s[i]=="[":
                st.append(s[i])
            else:
                if len(st)==0:
                    return False
                top=st.pop()
                if s[i]==')' and top!="(":
                    return False
                elif s[i]=='}' and top!="{":
                    return False
                elif s[i]==']' and top!="[":
                    return False
        return len(st)==0
