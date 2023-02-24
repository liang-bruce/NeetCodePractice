class MyHashMap:

    def __init__(self):
        self.map = []
        self.keySet = set()

    def put(self, key: int, value: int) -> None:
        if key in self.keySet:
            for i in range(len(self.map)):
                if key == self.map[i][0]:
                    self.map[i][1] = value
        else:
            self.map.append([key, value])
            self.keySet.add(key)

    def get(self, key: int) -> int:
        if key in self.keySet:
            for i in range(len(self.map)):
                if key == self.map[i][0]:
                    return self.map[i][1]
        return -1
        
    def remove(self, key: int) -> None:
        if key in self.keySet:
            for i in range(len(self.map)):
                if key == self.map[i][0]:
                    del self.map[i]
                    self.keySet.remove(key)
                    return
        return
