class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1: go through linked list and use a counter to record length
        #    then go from head again and stop in middle

        # 2: slow + fast ptrs
        # slow, fast = head, head
        # while fast.next and fast.next.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # return slow.next if fast.next else slow 

        # neetcode: faster because no if statement
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        return slow