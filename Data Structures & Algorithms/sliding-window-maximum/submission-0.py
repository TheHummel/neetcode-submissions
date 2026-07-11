class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n < k:
            return []

        neg_nums = [-x for x in nums]

        idx_map = {x: i for i, x in enumerate(nums)}

        res = []

        window = neg_nums[:k-1]
        heapq.heapify(window)

        i = 0

        while i+k <= n:
            print(i)
            heapq.heappush(window, neg_nums[i+k-1])
            cand = -window[0]
            while idx_map[cand] < i:
                heapq.heappop(window)
                cand = -window[0]

            res.append(cand)

            print(window, res)
            i+=1


        return res


