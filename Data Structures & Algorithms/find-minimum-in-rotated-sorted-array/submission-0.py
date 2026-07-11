class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1
        m = (r-l)//2

        while l < r:
            a = nums[l]
            b = nums[m]
            c = nums[r]

            if r-l == 1:
                return min(a,c)

            if c < b:
                l = m
            else:
                r = m
            m = l + (r-l)//2

        return  nums[l]
                
