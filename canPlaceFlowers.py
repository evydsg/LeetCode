class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        index = 0

        if n == 0:
            return True

        for index in range(len(flowerbed)):

            if flowerbed[index] == 0:
                prev_place = (index == 0 or flowerbed[index - 1] == 0)
                next_place = (index == len(flowerbed) - 1 or flowerbed[index +1] == 0)

                if prev_place and next_place:
                    flowerbed[index] = 1
                    n -= 1
                
                    if n == 0:
                        return True
        
        if n == 0:
            return True
        
        return False
        