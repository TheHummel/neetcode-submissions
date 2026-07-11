class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summe = sum(nums)
        if summe % 2 != 0:
            return False

        target = summe / 2

        n = len(nums)

        #dp = [[0 for i in range(target)] for j in range(n)]

        dp = [None for i in range(n+1)]
        dp[0] = {0}

        for i in range(1,n+1):
            dp[i] = dp[i-1].copy()
            num = nums[i-1]
            for ps in dp[i-1]:
                dp[i].add(num + ps)

            

        print(dp)

        return target in dp[n]