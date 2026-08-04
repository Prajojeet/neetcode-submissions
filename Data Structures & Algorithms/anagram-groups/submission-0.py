class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==0 or len(strs)==1:
            return[strs]

        counters = [{} for _ in range(len(strs))]
        for j,letter in enumerate(strs):
           for i in range(len(letter)):
                        if letter[i] not in counters[j]:
                            counters[j][letter[i]]=1
                        else:
                            counters[j][letter[i]]+=1
        
        i=0
        output=[]
        while(i<len(strs)):
            if strs[i]=='#':
                i+=1
                continue
            j=i
            temp=[]
            for j in range(len(strs)):
                if counters[i] == counters[j]:
                    temp.append(strs[j])
                    strs[j]='#'
            output.append(temp)
            i+=1

        return output
