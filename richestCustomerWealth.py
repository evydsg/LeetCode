class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        index, wealth = 0, 0
        
        for index in range(len(accounts)):
            wealth = max(wealth, sum(accounts[index]))
        
        return wealth