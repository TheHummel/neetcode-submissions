class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        n = len(beginWord)

        starMap = {} # starWord -> word
        wordsMap = {word: [] for word in wordList} # word -> starWord
        
        for word in wordList:
            for i in range(n):
                star = word[:i] + "*" + word[i+1:]
                if star in starMap:
                    starMap[star].append(word)
                else:
                    starMap[star] = [word]

                wordsMap[word].append(star)

        visited = set() # words
        visited.add(beginWord)
        q = deque() # words
        q.append((beginWord, 1))

        wordsMap[beginWord] = []

        for i in range(n):
            star = beginWord[:i] + "*" + beginWord[i+1:]
            wordsMap[beginWord].append(star)

            if star in starMap:
                starMap[star].append(beginWord)
            else:
                starMap[star] = [beginWord]


        print(wordsMap)
        print(starMap)

        while q:
            word, depth = q.popleft()

            depth += 1

            visited.add(word)

            starWords = wordsMap[word]
            print("round", word, starWords)

            for sw in starWords:
                words = starMap[sw]
                for word in words:
                    if word == endWord:
                        print("found")
                        return depth
                    if word not in visited:
                        q.append((word, depth))

        return 0
