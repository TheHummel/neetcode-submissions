class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        maxLen = 1
        n = len(s)

        j = 1
        curr = s[0]

        while j < n:
            c = s[j]
            if c in curr:
                i = curr.index(c)
                curr = curr[i+1:] + c

            else:
                curr += c
                maxLen = max(maxLen, len(curr))
                if maxLen == 31:
                    print(curr)

            j+=1

        return maxLen



                

