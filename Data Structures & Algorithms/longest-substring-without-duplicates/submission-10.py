class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = set()
        l = 0  
        longest = 0

        for r in range(len(s)):
            if s[r] not in counter:
                counter.add(s[r])
            else:
                while (s[l] != s[r]):
                    counter.remove(s[l])
                    l += 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest