class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, currSum):
            nonlocal targetSum
            if not root:
                return False

            currSum += root.val
            if not root.left and not root.right and currSum == targetSum:
                return True
            
            if dfs(root.left, currSum):
                return True 
            if dfs(root.right, currSum):
                return True
            currSum -= root.val
            return False
        
        return dfs(root, 0)