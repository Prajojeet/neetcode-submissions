class Solution:
    def isValid(self, s: str) -> bool:
        st=[]

        if len(s)%2!=0:
            return False
        
        for i in range(len(s)):
            if s[i]==']':
                if len(st) ==0 or st[-1]!='[':
                    return False
                st.pop()
            
            elif s[i]==')':
                if len(st) ==0 or st[-1]!='(':
                    return False
                st.pop()
            elif s[i]=='}':
                if len(st) == 0 or st[-1]!='{':
                    return False
                st.pop()
            
            else:
                st.append(s[i])
        return True if len(st)==0 else False