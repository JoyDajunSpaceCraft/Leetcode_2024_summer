class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return []
        adj = [set() for _ in range(n)]

        for v, u in edges:
            adj[v].add(u)
            adj[u].add(v)
        leaves = deque()
        for i in range(n):
            if len(adj[i])==1:
                leaves.append(i)
        while n>2:
            leaves_num = len(leaves)

            n-=leaves_num
            for i in range(leaves_num):
                leaf = leaves.popleft()
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                if len(adj[neighbor])==1:
                    leaves.append(neighbor)
        return list(leaves)
