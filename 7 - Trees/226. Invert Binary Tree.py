class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #2nd
        if not root:
            return 
        temp = root.right
        root.right = root.left
        root.left = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


        # if root == None:
        #     return None
       
        # tempNode = root.left
        # root.left = root.right
        # root.right = tempNode
        # self.invertTree(root.right)
        # self.invertTree(root.left)
        
        # return root