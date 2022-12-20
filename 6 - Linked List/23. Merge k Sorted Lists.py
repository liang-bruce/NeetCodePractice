# brute force O(kn), merge every list 1 by 1 using merge 2 sorted array
# faster O(nlog(k)), like merge sort
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mergedList = None

        while len(lists):
            mergedList = self.merge2Lists(lists.pop(),mergedList)

        return mergedList

    # faster solution
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     if not lists or len(lists) == 0:
    #         return None

    #     while len(lists) > 1:
    #         mergedLists = []
    #         for i in range(0, len(lists), 2):
    #             l1 = lists[i]
    #             l2 = lists[i + 1] if (i + 1) < len(lists) else None
    #             mergedLists.append(self.mergeList(l1, l2))
    #         lists = mergedLists
    #     return lists[0]

    def merge2Lists(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next