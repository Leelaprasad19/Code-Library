# LeetCode

class LRUCache:

    def __init__(self, capacity: int):
        self.d = dict()
        self.capacity = capacity
        
    def get(self, key: int) -> int:

        if(key not in self.d):
            return -1
        else:
            val = self.d[key]
            del self.d[key]
            self.d[key] = val
            return self.d[key]

    def put(self, key: int, value: int) -> None:

        if(key in self.d):
            del self.d[key]
        elif(len(self.d) == self.capacity):
            first_key = next(iter(self.d))
            del self.d[first_key]
        
        self.d[key] = value

        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
