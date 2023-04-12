class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, res):
            if not node:
                return
            
            dfs(node.left, res)
            dfs(node.right, res)
            res.append(node.val)
        
        res = []
        dfs(root, res)
        return res