# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr != None:
            curr = curr.next
            length += 1
        
        removePoint = length - n
        if removePoint == 0:
            head = head.next
            
        curr = head
        counter = 0
        while curr != None:
            counter += 1
            if counter == removePoint:
                curr.next = curr.next.next
                break
            curr = curr.next

        return head

# O(n) solution
# initiate right ptr n+1 space from left ptr, move both ptrs to tthe end of the list, left.next is the node to be removed.
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         dummy = ListNode(0, head)
#         left = dummy
#         right = head

#         while n > 0:
#             right = right.next
#             n -= 1

#         while right:
#             left = left.next
#             right = right.next

#         # delete
#         left.next = left.next.next
#         return dummy.next