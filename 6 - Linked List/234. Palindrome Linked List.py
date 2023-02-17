# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # O(n) Memory
        # cache = []
        # cur = head
        # while cur != None:
        #     cache.append(cur.val)
        #     cur = cur.next
        
        # l, r = 0, len(cache) - 1
        # while l < r:
        #     if cache[l] != cache[r]:
        #         return False
        #     l, r = l + 1, r - 1
        
        # return True

        # O(1) Memory
        # fast & slow ptrs to find the middle element
        # reverse the 2nd half of the list
        # compare 2 ptrs (head and prev)

        # find mid
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse 2nd half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        # compare pev and head
        cur = head
        while prev:
            if prev.val != cur.val:
                return False
            cur, prev = cur.next, prev.next
        
        return True