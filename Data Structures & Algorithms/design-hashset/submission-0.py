class MyHashSet:

    def __init__(self):
        self.size = 1000001
        self.hash_set = [0] * self.size

    def add(self, key: int) -> None:
        self.hash_set[key%self.size] = 1
        

    def remove(self, key: int) -> None:
        self.hash_set[key%self.size] = 0

    def contains(self, key: int) -> bool:
        return self.hash_set[key%self.size] == 1
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)