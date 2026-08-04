class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter={}
        for letter in strs:
            freq=[0]*26
            for char in letter:
                freq[ord(char)-ord('a')]+=1
            temp=tuple(freq)
            if temp not in counter:
                counter[temp]=[]
                counter[temp].append(letter)
            else:
                counter[temp].append(letter)
        output=[]
        for keys in counter:
            output.append(counter[keys])
        return output