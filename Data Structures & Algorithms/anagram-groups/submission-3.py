class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq_table = {} # May be store tuples with values as list of words
        
        for word in strs:
            freq = [0]*26
            # Calculating the frequency table
            for char in word:
                freq[ord(char) - ord('a')] += 1

            freq = tuple(freq)

            if freq not in freq_table:
                freq_table[freq] = [word]
            else:
                freq_table[freq].append(word)

        result = [item for item in freq_table.values()]
        return result
