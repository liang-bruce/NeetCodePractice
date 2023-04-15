# recursive dfs O(n): base case - when root is None, return 0; return 1 + max(left, right)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# https://www.youtube.com/watch?v=hTM3phVI6YQ
# iterative BFS O(n): use a queue to kepp track of levels
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = 0
        q = deque([root])
        while q:
            # for each level
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level +=1

        return level

# iterative DFS O(n): use a stack storing node & length to simulate call stack
 class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0

        stack = [[root,1]]
        res = 0
        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return res


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS
        depth, counter = 0, 0

        def dfs(node, counter):
            nonlocal depth
            if not node:
                depth = max(depth, counter)
                return

            counter += 1
            dfs(node.left, counter)
            dfs(node.right, counter)
        
        dfs(root, counter)
        return depth