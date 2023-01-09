class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        res = []

        while len(q):
            qLength = len(q)
            for i in range(qLength):
                curNode = q.popleft() 
                if curNode:
                    if curNode.left:
                        q.append(curNode.left)
                    if curNode.right:
                        q.append(curNode.right)
                    # operation for the rightmost Node only
                    if i == qLength - 1:
                        res.append(curNode.val)
        
        return res