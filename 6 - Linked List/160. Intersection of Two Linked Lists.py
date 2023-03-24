# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # O(n+m), O(n)
        # ptr1, ptr2 = headA, headB
        # LL1= set()
        # while ptr1:
        #     LL1.add(ptr1)
        #     ptr1 = ptr1.next
        
        # while ptr2:
        #     if ptr2 in LL1:
        #         return ptr2
        #     ptr2 = ptr2.next
        
        # return None

        # O(n+m), O(1)
        ptr1, ptr2 = headA, headB

        while ptr1 != ptr2:
            ptr1 = ptr1.next if ptr1 else headB
            ptr2 = ptr2.next if ptr2 else headA
        
        return ptr1