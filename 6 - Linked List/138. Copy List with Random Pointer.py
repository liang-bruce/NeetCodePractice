class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # use a dictionary to store the copies
        # need to initialize as {None: None} because null (end of list) will not execute 
        copy = {None: None}

        cur = head
        while cur:
            copy[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            copy[cur].next = copy[cur.next]
            copy[cur].random = copy[cur.random]
            cur = cur.next
        
        return copy[head]