class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None

        q = deque([root])
        result = []

        while len(q):
            currLevelNodes = []
            for i in range(len(q)):
                currNode = q.popleft()
                currLevelNodes.append(currNode.val)
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
                
            result.append(currLevelNodes)

            
        
        return result