class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        nums_sorted = sorted(nums)

        n = len(nums)

        i = 0
        j = 1

        for i, num in enumerate(nums_sorted):
            j = i+1
            k = n-1
            while j < k:
                num_j = nums_sorted[j]
                num_k = nums_sorted[k]

                if num + num_j + num_k < 0:
                    j += 1
                elif num + num_j + num_k > 0:
                    k -= 1
                else:
                    res.add((num, num_j, num_k))
                    j+=1

        
        return list(res)

        