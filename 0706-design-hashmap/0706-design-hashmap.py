class MyHashMap:

    def __init__(self):
        self.buckets = [[] for i in range(1009)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % 1009
        for i in self.buckets[hash_key]:
            if key == i[0]:
                i.pop()
                i.append(value)
                return
        self.buckets[hash_key].append([key, value])

    def get(self, key: int) -> int:
        hash_key = key % 1009
        for i in self.buckets[hash_key]:
            if key == i[0]:
                return i[-1]
        return -1
        

    def remove(self, key: int) -> None:
        hash_key = key % 1009
        for i in self.buckets[hash_key]:
            if key == i[0]:
                self.buckets[hash_key].remove(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)