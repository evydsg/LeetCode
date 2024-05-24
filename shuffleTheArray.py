class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x_nums = nums[:n]
        y_nums = nums[n:]
        shuffled_nums = []

        for index in range(n):
            shuffled_nums.append(x_nums[index])
            shuffled_nums.append(y_nums[index])

        
        return shuffled_nums
