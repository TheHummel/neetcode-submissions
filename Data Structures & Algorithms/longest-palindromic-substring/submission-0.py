class Solution:
    def longestPalindrome(self, s: str) -> str:
        """n = len(s)

        dp = [[1]]

        for i in range(1, n):
            c = s[i]

            prevMaxes = dp[i-1]
            
            cand = [1]

            for prevMax in prevMaxes:
                if prevMax == 1:
                    if s[i-1] == c:
                        cand += [2]
                
                elif i - prevMax - 1 >= 0 and s[i - prevMax - 1] == c:
                    cand += [prevMax + 2]
            
            dp.append(cand)

        maxes = [max(cands) for cands in dp]

        return max(maxes)"""

        n = len(s)
        res = ""

        for i in range(n):
            j = 1

            while i - j >= 0 and i + j < n and s[i-j] == s[i+j]:
                j+=1
            j-=1

            if 2*j + 1 > len(res):
                res = s[i-j:i+j+1]

            if i < n-1:
                if s[i] == s[i+1]:
                    j = 1
                    while i - j >= 0 and i + j + 1 < n and s[i-j] == s[i+j + 1]:
                        j+=1
                    j-=1
                    if 2*j + 2 > len(res):
                        res = s[i-j:i+j+2]

        return res

