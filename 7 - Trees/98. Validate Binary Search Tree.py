class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        maxVal = float('inf')
        minVal = float('-inf')

        return self.isValidBSTHelper(root, maxVal, minVal)


    def isValidBSTHelper(self, node, maxVal, minVal):
        if not node:
            return True
        
        if node.val > minVal and node.val < maxVal:
            return self.isValidBSTHelper(node.left, node.val, minVal) and self.isValidBSTHelper(node.right, maxVal, node.val)
        else:
            return False