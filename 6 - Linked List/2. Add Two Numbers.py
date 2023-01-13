# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur1, cur2, curNew = l1, l2, dummy
        moving = 0

        while cur1 and cur2:
            if moving == 1:
                curVal = cur1.val + cur2.val + moving
                moving = 0
            else:
                curVal = cur1.val + cur2.val

            if curVal >= 10:
                curVal -= 10
                moving = 1

            curNew.next = ListNode(curVal)
            curNew = curNew.next
            cur1 = cur1.next
            cur2 = cur2.next
            # print(curNew.val, curVal)
        
        left = cur1 if cur1 else cur2

        while left:
            if moving == 1:
                curVal = left.val + moving
                moving = 0
            else:
                curVal = left.val

            if curVal >= 10:
                curVal -= 10
                moving = 1

            curNew.next = ListNode(curVal)
            curNew = curNew.next
            left = left.next
            # print(curNew.val, curVal)

        if moving == 1:
            curNew.next = ListNode(1)
            curNew = curNew.next
        curNew.next = None
        
        return dummy.next

# same idea, more readable
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         dummy = ListNode()
#         cur = dummy

#         carry = 0
#         while l1 or l2 or carry:
#             v1 = l1.val if l1 else 0
#             v2 = l2.val if l2 else 0

#             # new digit
#             val = v1 + v2 + carry
#             carry = val // 10
#             val = val % 10
#             cur.next = ListNode(val)

#             # update ptrs
#             cur = cur.next
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None

#         return dummy.next