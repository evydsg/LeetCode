class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length, index = len(s)-1, 0

        while index < length:
            temporary = s[index]
            s[index], s[length] = s[length], temporary

            index+=1
            length-=1