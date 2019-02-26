import time


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.container = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.container.keys():
            return -1

        self.container[key][0] += 1  # count
        self.container[key][1] = time.time() # access time

        # todo sort dict according to container[key][0] and container[key][1]
        sorted(self.container.items(), key=lambda x: x[1])

        return self.container[key][2]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if (self.capacity <= 0):
            return

        if key in self.container.keys():
            self.container[key][0] += 1  # count
            self.container[key][1] = time.time()  # access time
            self.container[key][2] = value

        else:
            if len(self.container) > self.capacity:
                self.container.pop(self.container.keys())
            self.container[key] = []
            self.container[key].append(0)  # count
            self.container[key].append(time.time())  # count
            self.container[key].append(value)  # count

        sorted(self.container.items(), key=lambda x: x[1])

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    # print([1,2,3] > [0,1,3])
    # cache = LFUCache(2)
    # cache.put(1, 1);
    # cache.put(2, 2);
    # cache.get(1);
    # cache.put(3, 3)
    # cache.get(2);
    # cache.get(3);
    # cache.put(4, 4);
    #
    # cache.get(1);
    # cache.get(3);
    # cache.get(4);

    lista = [2,3,2,1,2]
    lista.sort()
    print(lista)
