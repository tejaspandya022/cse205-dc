class MyHashSet:
    d = {}
    def __init__(self):
        self.d={}
        

    def add(self, key: int) -> None:
        self.d[key]=1
        

    def remove(self, key: int) -> None:
        if key in self.d:
            self.d.pop(key)
        

    def contains(self, key: int) -> bool:
        if key in self.d:
            return True
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)