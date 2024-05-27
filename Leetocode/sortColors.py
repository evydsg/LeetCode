class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_colors = [0, 0 , 0]

        for color in nums:
            if color == 0:
                count_colors[0] += 1
            elif color == 1:
                count_colors[1] += 1
            elif color == 2:
                count_colors[2] += 1 

        index = 0
        for color in range(len(count_colors)):
            for colors in range(count_colors[color]):
                nums[index] = color
                index+=1