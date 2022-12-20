# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head
        nodeDeque = deque()
        while curr.next != None:
            curr = curr.next
            nodeDeque.append(curr)
        
        curr = head
        counter = 0
        while len(nodeDeque) > 0:
            counter += 1
            if counter % 2 == 0:
                curr.next = nodeDeque.popleft()
            else:
                curr.next = nodeDeque.pop()
            curr = curr.next
        
        curr.next = None

# O(1) space solution
# class Solution:
#     def reorderList(self, head: ListNode) -> None:
#         # find middle
#         slow, fast = head, head.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#         # reverse second half
#         second = slow.next
#         prev = slow.next = None
#         while second:
#             tmp = second.next
#             second.next = prev
#             prev = second
#             second = tmp

#         # merge two halfs
#         first, second = head, prev
#         while second:
#             tmp1, tmp2 = first.next, second.next
#             first.next = second
#             second.next = tmp1
#             first, second = tmp1, tmp2