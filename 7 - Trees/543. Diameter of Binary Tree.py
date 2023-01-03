# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        currMax = 0
        def dfs(node):
            nonlocal currMax
            
            if not node:
                return -1
            currLeft = dfs(node.left)
            currRight = dfs(node.right)
            currMax = max(currMax, (currLeft + 1) + (currRight + 1))

            return max(currLeft + 1, currRight + 1)
        
        dfs(root)
        return currMax