class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        revStack = []

        n = len(temperatures)

        res = deque()

        for i in range(n):
            temp = temperatures[n-i-1]
            nextBiggest = -1
            while revStack:
                cand_idx = revStack.pop()
                cand = temperatures[n-cand_idx-1]
                print(f"checking {cand} for {temp}")
                if cand > temp:
                    print("hit")
                    nextBiggest = i - cand_idx
                    revStack.append(cand_idx)
                    break
            print(i, temp, nextBiggest, revStack)
            res.appendleft(0 if nextBiggest == -1 else nextBiggest)
            revStack.append(i)

        return list(res)
