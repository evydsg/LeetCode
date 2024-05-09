class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.split()
        last_word = s_list[-1]
        return len(last_word)