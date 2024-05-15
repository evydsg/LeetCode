class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        first = 1
        second = 2

        for iteration in range(3, n+1):
            current_iteration = first + second
            first = second
            second = current_iteration

        return second