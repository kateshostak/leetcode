class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_freq = {}
        self.freq_to_key = {}
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cash:
            freq = self.key_to_freq[key]
            self.freq_to_key[freq].remove(key)
            if not self.freq_to_key[freq]:
                self.freq_to_key.remove(freq)

            if freq + 1 in self.freq_to_key:
                self.freq_to_key[freq + 1].append(key)
            else:
                self.freq_to_key[freq + 1] = []
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cash) >= self.capacity:
            min_freq = min(self.freq_to_key)
            elem = self.freq_to_key[min_freq].pop()
            self.cache.remove(elem)
            if not self.freq_to_key[min_freq]:
                self.freq_to_key.remove(min_freq)
        self.key_to_freq[key] = 0
        self.cache[key] = value


def main():
    cash = LRUCache(2)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
