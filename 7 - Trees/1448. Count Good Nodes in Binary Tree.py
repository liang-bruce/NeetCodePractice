class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, curMin):
            nonlocal count
            if not node:
                return
            if node.val >= curMin:
                count += 1
            curMin = max(curMin, node.val)
            dfs(node.left, curMin)
            dfs(node.right, curMin)
        
        dfs(root, float('-inf'))
        return count