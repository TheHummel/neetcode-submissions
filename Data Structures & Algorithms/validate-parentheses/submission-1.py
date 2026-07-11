class Solution:
    def isValid(self, s: str) -> bool:
        stack = ""

        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack += c
                continue
            if not stack:
                return False
            
            stack, popped = stack[:-1], stack[-1]
            if (c == ")" and popped != "(") or (c == "}" and popped != "{") or (c == "]" and popped != "["):
                return False

        if stack:
            return False
        return True
        