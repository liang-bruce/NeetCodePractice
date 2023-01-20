class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        nodeMap = {}

        def dfs(node):
            if node in nodeMap:
                return nodeMap[node]
            
            copy = Node(node.val)
            nodeMap[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
            
        return dfs(node) if node else None