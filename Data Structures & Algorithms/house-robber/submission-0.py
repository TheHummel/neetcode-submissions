class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        n = len(nums)
        dp = nums[:2]
        dp.append(dp[0] + nums[2])

        for i in range(3, n):
            num = nums[i]
            dp.append(max(dp[i-2], dp[i-3]) + num)

        return max(dp)