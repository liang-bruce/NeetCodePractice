class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # cur = head
        # while cur and cur.next:
        #     if cur.next.val == cur.val:
        #         cur.next = cur.next.next
        #         continue
        #     cur = cur.next
        
        # return head

        #this is faster, less operation
        cur = head
        while cur:
            # use a nested while loop to get rid of continuous duplicates
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head