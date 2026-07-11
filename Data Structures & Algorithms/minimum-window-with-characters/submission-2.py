class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = {}
        for c in t:
            t_freq[c] = t_freq.get(c, 0) + 1

        print(t_freq)

        curr_freq = {}

        min_curr = ""

        have = 0
        need = len(t_freq)

        min_len = 1001
        i = 0

        for j, c in enumerate(s):

            print(c, curr_freq)

            if c in t_freq:
                curr_freq[c] = curr_freq.get(c, 0) + 1
                if curr_freq[c] == t_freq[c]:
                    have += 1

                while have == need:
                    i_char = s[i]

                    curr_snippet = s[i:j+1]
                    length = len(curr_snippet)

                    if length < min_len:
                            min_len = length
                            min_curr = curr_snippet

                    if i_char in t_freq and i_char in curr_freq:
                        curr_freq[i_char] -= 1
                        if curr_freq[i_char] < t_freq[i_char]:
                            have -= 1

                    i+=1

                    """if i_char in t_freq:
                        curr_snippet = s[i:j+1]
                        length = len(curr_snippet)

                        print(curr_freq, curr_snippet, length)
                        if length < min_len:
                            min_len = length
                            min_curr = curr_snippet
                        break
                    i+=1"""

                """if curr_freq[c] > t_freq[c]:
                    print("1")
                    while curr_freq[c] > t_freq[c]:
                        i_char = s[i]
                        if i_char in curr_freq:
                            if i_char in t_freq and curr_freq[i_char] == t_freq[i_char]:
                                break
                            curr_freq[i_char] -= 1
                        i+=1
                    print(curr_freq)


                if curr_freq == t_freq:
                    print("2")
                    while True:
                        i_char = s[i]
                        if i_char in t_freq:
                            curr_snippet = s[i:j+1]
                            length = len(curr_snippet)

                            print(curr_freq, curr_snippet, length)
                            if length < min_len:
                                min_len = length
                                min_curr = curr_snippet
                            break
                        i+=1"""
                        

        return min_curr
                    





        