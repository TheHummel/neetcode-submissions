class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0

        count = {}
        maxF = 0

        l = 0

        for i, c in enumerate(s):
            count[c] = 1 + count.get(c, 0)

            maxF = max(maxF, count[c])

            while (i-l+1) - maxF > k:
                print(i, c, count)
                count[s[l]] -= 1
                l+=1

            print("f", i, c, count)
            
            res = max(res, i-l+1)

        return res
