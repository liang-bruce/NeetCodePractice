class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
       
        tempNode = root.left
        root.left = root.right
        root.right = tempNode
        self.invertTree(root.right)
        self.invertTree(root.left)
        
        return root