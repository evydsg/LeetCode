class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0
        index = 0

        for index in range(len(nums)):
            if nums[index] == val:
                continue
            else:
                number = nums[index]
                nums[k] = number
                k+=1

        return k