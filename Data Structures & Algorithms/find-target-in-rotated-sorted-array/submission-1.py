class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1
        l = 0
        r = n - 1
        m = (r-l) // 2

        count = 0

        while l < r:
            a = nums[l]
            b = nums[m]
            c = nums[r]
            if r - l == 1:
                if a == target:
                    return l
                elif c == target:
                    return r
                return -1

            
            if target == a:
                return l
            if target == b:
                return m
            if target == c:
                return r
            #if target < b and target > a:

            if c < b:
                if target < c or target > b:
                    l = m
                else:
                    r = m
            else:
                if target < b or target > a:
                    r = m
                else:
                    l = m
            m = l+(r-l) // 2

            print(l, m, r)
            count += 1
            if count > 20:
                return -1

        return -1
                



        