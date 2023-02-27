class ListNode():
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    # def __init__(self):
    #     self.map = []
    #     self.keySet = set()

    # def put(self, key: int, value: int) -> None:
    #     if key in self.keySet:
    #         for i in range(len(self.map)):
    #             if key == self.map[i][0]:
    #                 self.map[i][1] = value
    #     else:
    #         self.map.append([key, value])
    #         self.keySet.add(key)

    # def get(self, key: int) -> int:
    #     if key in self.keySet:
    #         for i in range(len(self.map)):
    #             if key == self.map[i][0]:
    #                 return self.map[i][1]
    #     return -1

    # def remove(self, key: int) -> None:
    #     if key in self.keySet:
    #         for i in range(len(self.map)):
    #             if key == self.map[i][0]:
    #                 del self.map[i]
    #                 self.keySet.remove(key)
    #                 return
    #     return
    

    def __init__(self):
        self.map = [ListNode() for i in range(1000)]
        
    def hash(self, key):
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.map[self.hash(key)].next
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

        
    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)]
        while cur and cur.next: # 2 conditions because we want ptr manipulation
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        return