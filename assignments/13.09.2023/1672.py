class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth=[]
        for i in accounts:
            count=0
            for j in i:
                count+=j
            wealth.append(count)
        return max(wealth)

        