class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        prefix_maxes = []
        prefix_max = 0

        suffix_maxes = []
        suffix_max = 0

        for i in range(n):
            prefix_maxes.append(prefix_max)
            suffix_maxes = [suffix_max] + suffix_maxes

            prefix_max = max(prefix_max, height[i])
            suffix_max = max(suffix_max, height[n-i-1])

        total = 0

        print(prefix_maxes)
        print(suffix_maxes)
        maxes = []

        for i in range(n):
            total += max(min(prefix_maxes[i], suffix_maxes[i]) - height[i], 0)
            maxes.append(min(prefix_maxes[i], suffix_maxes[i]) - height[i])

        print(maxes)

        
        return total

        
        


        