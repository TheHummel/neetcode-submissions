class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}

        for s_ in s:
            if s_ in freq1:
                freq1[s_] += 1
            else:
                freq1[s_] = 1

        for t_ in t:
            if t_ in freq2:
                freq2[t_] += 1
            else:
                freq2[t_] = 1

        if len(freq1.keys()) != len(freq2.keys()):
            return False

        for c in freq1.keys():
            if c not in freq2:
                return False
            if freq1[c] != freq2[c]:
                return False

        return True
        