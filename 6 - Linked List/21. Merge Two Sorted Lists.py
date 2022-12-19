class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None or list2 == None:
            if list1 != None:
                return list1
            if list2 != None:
                return list2
            return None

        head = list1 if list1.val <= list2.val else list2

        curr = head
        curr1 = list1.next if curr == list1 else list1
        curr2 = list2.next if curr == list2 else list2

        while (curr1 != None) and (curr2 != None):
            if curr1.val <= curr2.val:
                curr.next = curr1
                curr = curr.next
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr = curr.next
                curr2 = curr2.next
        
        while curr1 != None:
            curr.next = curr1
            curr = curr.next
            curr1 = curr1.next
        
        while curr2 != None:
            curr.next = curr2
            curr = curr.next
            curr2 = curr2.next
        
        return head

    # shorter solution
    # def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
    #     dummy = ListNode()
    #     tail = dummy

    #     while list1 and list2:
    #         if list1.val < list2.val:
    #             tail.next = list1
    #             list1 = list1.next
    #         else:
    #             tail.next = list2
    #             list2 = list2.next
    #         tail = tail.next

    #     if list1:
    #         tail.next = list1
    #     elif list2:
    #         tail.next = list2

    #     return dummy.next