class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # cache = {}
        # counter, length, curSum, res = 0, 0, 0, 0
        # curNode = head

        # while curNode:
        #     length += 1
        #     curNode = curNode.next

        # half = (length) / 2 - 1
        # curNode = head
        # while curNode:
        #     if counter <= (half):
        #         twin = length - 1 - counter
        #         cache[twin] = curNode.val
        #     else:
        #         curSum = cache[counter] + curNode.val
        #         res = max(res, curSum)

        #     curNode = curNode.next
        #     counter += 1
        
        # return res

        # O(1) space.
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            # think below 4 lines is reversing the first half of the LL and moving slow forward
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        res = 0
        while slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        return res