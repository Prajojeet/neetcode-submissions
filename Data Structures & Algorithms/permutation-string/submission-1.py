class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Simple in any 3 slider window, if frequency matches return true

        # Edge Case 
        if len(s1)>len(s2):
            return False

        # Conversion to hashmap
        hashmap_s1={}
        for char in s1:
            if char not in hashmap_s1:
                hashmap_s1[char]=1
            else:
                hashmap_s1[char]+=1

        hashmap_compare={}
        
        # For first 3 elements in s2:
        length_s1=len(s1)
        length_s2=len(s2)
        for i in range(length_s2):
            # Iteration upto the base number of elements in s1
            if i<length_s1:
                if s2[i] not in hashmap_compare:
                    hashmap_compare[s2[i]]=1
                else:
                    hashmap_compare[s2[i]]+=1
            else:
                # Base check in each window
                if hashmap_s1==hashmap_compare:
                    return True

                # deletion of past element
                if hashmap_compare[s2[i-length_s1]]==1:
                    hashmap_compare.pop(s2[i-length_s1])
                else:
                    hashmap_compare[s2[i-length_s1]]-=1

                # Addition of current element
                if not s2[i] in hashmap_compare:
                    hashmap_compare[s2[i]]=1
                else:
                    hashmap_compare[s2[i]]+=1
       
        if hashmap_compare==hashmap_s1:
            return True
        else:
            return False
            
                
