class Solution:
    def isValid(self, s: str) -> bool:

        parentheses ={')': '(', '}': '{', ']': '['}
        stack = []
        answer = False
        index = 0

        for index in range(len(s)):
            if s[index] in parentheses:
                if len(stack) != 0 and parentheses[s[index]] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[index])
        
        if len(stack) == 0:
            return True
        
        return answer
