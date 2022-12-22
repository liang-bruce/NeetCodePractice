class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return self.isIdentical(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isIdentical(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        else:
            return self.isIdentical(p.left, q.left) and self.isIdentical(p.right, q.right)

# class Solution:
#     def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
#         if not t:
#             return True
#         if not s:
#             return False

#         if self.sameTree(s, t):
#             return True
#         return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

#     def sameTree(self, s, t):
#         if not s and not t:
#             return True
#         if s and t and s.val == t.val:
#             return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
#         return False