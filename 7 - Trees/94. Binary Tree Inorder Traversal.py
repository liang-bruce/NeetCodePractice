class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(root, res):
            if not root:
                return
            
            dfs(root.left, res)
            res.append(root.val)
            dfs(root.right, res)
        
        res = []
        dfs(root, res)
        return res