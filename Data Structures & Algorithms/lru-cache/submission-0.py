class LRUCache:
    """Given - capacity, get, put -> need to design it so i could remove the least used cache """
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.limit = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]


    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if self.limit < len(self.cache):
            self.cache.popitem(last = False)