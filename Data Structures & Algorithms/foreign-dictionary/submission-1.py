class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        edges = defaultdict(set)

        alphabet = {c for word in words for c in word}
        in_deg = {c : 0 for c in alphabet}

        for i in range(n-1):
            w1 = words[i]
            w2 = words[i+1]
            m = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:m] == w2[:m]:
                return ""

            for j in range(m):
                if w1[j] != w2[j]:
                    if w2[j] not in edges[w1[j]]:
                        edges[w1[j]].add(w2[j])
                        in_deg[w2[j]] += 1
                    break

        queue = deque(sorted({c for c in alphabet if in_deg[c] == 0}))
        res = []
        while queue:
            c = queue.popleft()
            res.append(c)
            for nxt in edges[c]:
                in_deg[nxt] -=1
                if in_deg[nxt] < 1:
                    queue.append(nxt)

        return "".join(res) if len(res) == len(alphabet) else ""