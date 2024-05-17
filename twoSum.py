class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        dictionary = {}

        for index in range(len(nums)):
            nums2 = target - nums[index]
            
            if nums2 in dictionary:
                answer.append(index)
                answer.append(dictionary[nums2])

            dictionary[nums[index]] = index
        
        return answer
        