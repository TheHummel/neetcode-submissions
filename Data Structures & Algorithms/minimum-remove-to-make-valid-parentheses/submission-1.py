class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = deque()

        stack = 0

        res = ""

        for c in s:
            if c == "(":
                stack += 1
                res += c
            elif c == ")":
                if stack >= 1:
                    stack -= 1
                    res += c
            else:
                res += c

        i = len(res) - 1
        while stack and i >= 0:
            if res[i] == "(":
                res = res[:i] + res[i+1:]
                stack -= 1
            i -= 1


        return res
