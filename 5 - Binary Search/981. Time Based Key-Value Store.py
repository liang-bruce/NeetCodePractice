# use binary search (update when values[m][1] <= timestamp) - O(log(n))
# {key: [[time, value]]} - O(k)(k is the len of list)
# {key: {time: value}} - O(n) n is the timestamp

# from collections import defaultdict
# class TimeMap:

#     def __init__(self):
#         self.timeMap = defaultdict(list)

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         self.timeMap[key].append([timestamp, value])

#     def get(self, key: str, timestamp: int) -> str:
#         if key not in self.timeMap:
#             return ""
#         for i in range(len(self.timeMap[key]) - 1, -1, -1):
#             if self.timeMap[key][i][0] <= timestamp:
#                 return self.timeMap[key][i][1]
#         return ""

class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyStore = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)