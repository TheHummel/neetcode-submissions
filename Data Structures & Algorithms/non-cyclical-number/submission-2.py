class Solution:
    def isHappy(self, n: int) -> bool:
        def calcSumSquares(i):
            digits = [int(d) for d in str(abs(i))]
            print(i, digits, [d**2 for d in digits])
            return sum([d**2 for d in digits])

        hashSet = {n}

        curr = n
        while True:
            curr = calcSumSquares(curr)
            if curr == 1:
                return True
            elif curr in hashSet:
                return False
            hashSet.add(curr)

    