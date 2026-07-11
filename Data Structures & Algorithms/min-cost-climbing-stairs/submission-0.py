class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0, 0]
        cost.append(0)
        n = len(cost)

        for i in range(2, n):
            dp.append(min(cost[i-1]+dp[i-1], cost[i-2]+dp[i-2]))

        return dp[-1]