class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n < k:
            return []

        neg_nums = [-x for x in nums]

        #idx_map = {x: i for i, x in enumerate(nums)}

        res = []

        window = []

        
        for i in range(k-1):
            heapq.heappush(window, (neg_nums[i], i))

        print(window)

        i = 0

        while i+k <= n:
            print(i)
            heapq.heappush(window, (neg_nums[i+k-1], i+k-1))
            cand, cand_idx = window[0]
            while cand_idx < i:
                heapq.heappop(window)
                cand, cand_idx = window[0]

            res.append(-cand)

            print(window, res)
            i+=1


        return res


