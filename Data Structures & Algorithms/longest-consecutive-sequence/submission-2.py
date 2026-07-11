class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        maxim = 0

        for num in num_set:
            prev = num - 1
            if prev not in num_set:
                l = 1
                while num + l in num_set:
                    l += 1
                maxim = max(maxim, l)

        return maxim