class MyHashMap:

    def __init__(self):
        self.size = 1009
        self.hash_map = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        tuples = self.hash_map[idx]
        for k, v in tuples:
            if k == key:
                self.hash_map[idx].remove((k, v))

        self.hash_map[idx].append((key, value))

    def get(self, key: int) -> int:
        idx = self._hash(key)
        tuples = self.hash_map[idx]
        for k, v in tuples:
            if k == key:
                return v

        return -1
        

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        tuples = self.hash_map[idx]
        for k, v in tuples:
            if k == key:
                self.hash_map[idx].remove((k, v))
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)