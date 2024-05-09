class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        longest = 0
        index = 0

        for index in range(len(s)):
            if s[index] != " ":
                length += 1
                longest = length
            
            else:
                length = 0
            
        if length > longest:
            return length
        
        return longest