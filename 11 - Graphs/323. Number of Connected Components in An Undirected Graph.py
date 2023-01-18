# Union Find
class Solution:
	# initially each node is unconnected, n separate components
	# each node with rank == 1 and parent is itself
	par = [i for i in range(n)]
	rank = [1] * n

	def find(node):
		res = node

		while res != par[res]:
			par[res] = par[par[res]] # this only speeds up the algo
			res = par[res]

		return res

	def union(node1, node2):
		p1, p2 = find(node1), find(node2)

		if p1 == p2:
			return 0

		if rank[p2] > rank[p1]:
			par[p1] = p2
			rank[p2] += rank[p1]
		else:
			par[p2] = p1
			rank[p1] += rank[p2]
		return p

	res = n
	for node1, node2 in edges:
		res -= union(node1, node2)
		
	return res