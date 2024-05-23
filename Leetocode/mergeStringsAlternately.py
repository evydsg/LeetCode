class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = []
        index = 0
        
        for index in range(min(len(word1), len(word2))):
            new_string.append(word1[index])
            new_string.append(word2[index])
        
        if len(word1) > len(word2):
            new_string.append(word1[index + 1:])
        else:
            new_string.append(word2[index + 1:])
        
        return "".join(new_string)