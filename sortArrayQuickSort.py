class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length =len(nums)
        mid_length = length//2

        if length <=1:
            return nums
        
        pivot_elem = nums[mid_length]

        left_elem = [num for num in nums if num < pivot_elem]
        middle = [num for num in nums if num == pivot_elem]
        right_elem = [num for num in nums if num > pivot_elem]

        return self.sortArray(left_elem) + middle + self.sortArray(right_elem)