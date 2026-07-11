class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        words = {}

        for word in strs:
            chars = "".join(sorted(word))
            if chars in words.keys():
                words[chars] += [word]
            else:
                words[chars] = [word]

        result = [words[key] for key in words.keys()]

        print("all keys", words.keys())
        
        return result
        