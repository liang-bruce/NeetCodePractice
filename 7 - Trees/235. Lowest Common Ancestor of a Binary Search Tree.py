class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # It is a BST, left > node > right, so LCA must be in the middle or being 1 of p/ q
        curr = root
        
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right 
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr 