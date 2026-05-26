class LRUCache:

    # least used
    # first in first out; queue
    

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = OrderedDict()
        

    def get(self, key: int) -> int:
        if key in self.hash:
            self.hash.move_to_end(key, last=True) # move to end as recently used
            return self.hash[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.hash[key] = value
            self.hash.move_to_end(key, last=True)
            return

        if len(self.hash) >= self.capacity:
            # remove least recently used
            self.hash.popitem(last=False)

        # add new key
        self.hash[key] = value
        self.hash.move_to_end(key, last=True)