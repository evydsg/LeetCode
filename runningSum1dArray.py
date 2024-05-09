class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        Sum = 0

        for num in nums:
            Sum += num
            answer.append(Sum)
        return answer