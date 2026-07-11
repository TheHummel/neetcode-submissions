class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """n = len(nums)
        if n < k:
            return []

        neg_nums = [-x for x in nums]

        #idx_map = {x: i for i, x in enumerate(nums)}

        res = []

        window = []

        
        for i in range(k-1):
            heapq.heappush(window, (neg_nums[i], i))


        i = 0

        while i+k <= n:
            heapq.heappush(window, (neg_nums[i+k-1], i+k-1))
            cand, cand_idx = window[0]
            while cand_idx < i:
                heapq.heappop(window)
                cand, cand_idx = window[0]

            res.append(-cand)

            i+=1


        return res"""

        n = len(nums)

        res = []

        #window = nums[:k-1]

        q = deque()

        #for el in window:
        #    q.append(el)

        i = 0

        while i < n:
            while q and q[0] < i - k + 1:
                q.popleft()

            while q and nums[i] > nums[q[-1]]:
                q.pop()

            q.append(i)

            if i >= k-1:
                res.append(nums[q[0]])

            i+=1

        return res


