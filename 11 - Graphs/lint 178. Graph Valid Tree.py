class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:

        par = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            p = par[node]

            while p != par[p]:
                p = par[p]
            return p
        
        def union(node1, node2):
            p1, p2 = find(node1), find(node2) 

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            
            return True

        connected = n
        for node1, node2 in edges:
            if not union(node1, node2):
                return False
            else:
                connected -= 1
        if connected > 1:
            return False
        return True