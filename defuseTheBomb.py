class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        length = len(code)
        
        if k == 0:
            return [0] * length

        answer = []
        total = 0

        if k > 0:
            for index in range(length):
                total = 0
                for second_index in range(1, k + 1):
                    total += code[(index + second_index) % length]
                
                answer.append(total)
        elif k < 0:
            for index in range(length):
                total = 0
                for second_index in range(1, - k + 1):
                    total += code[(index - second_index) % length]
                
                answer.append(total)
        
        return answer