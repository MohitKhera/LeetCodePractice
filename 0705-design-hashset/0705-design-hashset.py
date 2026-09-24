class MyHashSet:

    def __init__(self):
        self.buckets = [[] for i in range(10)]

    def add(self, key: int) -> None:
        bucket = key % 10
        if key not in self.buckets[bucket]:
            self.buckets[bucket].append(key)

    def remove(self, key: int) -> None:
        bucket = key % 10
        if key not in self.buckets[bucket]:
            return
        else:
            self.buckets[bucket].remove(key)

    def contains(self, key: int) -> bool:
        bucket = key % 10
        return key in self.buckets[bucket]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
