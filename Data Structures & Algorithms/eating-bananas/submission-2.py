class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)

        def check(k):
            summe = 0
            for pile in piles:
                summe += math.ceil(pile/k)
                if summe > h:
                    return False

            return summe <= h

        lo, hi = 1, m
        while lo < hi:
            mid = (hi + lo) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo