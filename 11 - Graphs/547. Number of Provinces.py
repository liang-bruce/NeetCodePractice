class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        par = [i for i in range(len(isConnected))] # node start from 0 not 1
        rank = [1] * len(isConnected)

        def find(node):
            res = node

            while res != par[res]:
                res = par[res]
            return res
        
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)

            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return 1
        
        res = len(isConnected)
        for i in range(len(isConnected)):
            node1 = i
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    node2 = j
                    res -= union(node1, node2)
        
        return res
