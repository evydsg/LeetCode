class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel = [character for character in jewels]
        count = 0

        for stone in stones:
            if stone in jewel:
                count += 1
            
        return count