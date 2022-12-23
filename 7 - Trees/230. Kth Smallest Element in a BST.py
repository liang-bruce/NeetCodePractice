class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inOrderList = self.getInOrderList(root, [])
        return inOrderList[k - 1]


    def getInOrderList(self, node, inOrderList):
        if node.left:
            self.getInOrderList(node.left, inOrderList)
        
        inOrderList.append(node.val)

        if node.right:
            self.getInOrderList(node.right, inOrderList)
        
        return inOrderList

# 
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right