class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        freq = {}
        longest = 0
        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]] = 1
            else:
                freq[s[r]] +=1
             
            if (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            
            else:
                longest = max(longest, r - l + 1)

        return longest