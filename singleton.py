class b:
    _inst = None
    _CacheMap = {}
    def __new__(cls, *args):
        print("newb is called")
        if(cls._inst is None):
            cls._inst = super().__new__(cls)
        return cls._inst
    
    def __init__(self, a=0):
        print("initb is called")
        self.a = a
        # print(self.a)
    
    def set_map(self, k,v):
        self._CacheMap[k] = v
    
    def get_map(self):
        return self._CacheMap
obj1 = b()
obj2 = b(1)
obj1.set_map("a", 1)
obj2.set_map("b", 2)
print(obj1.a)
print(obj1.get_map())