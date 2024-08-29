class Solution:
    # def removeStones(self, stones: List[List[int]]) -> int:
    def removeStones(self,stones):
        uf = UnionFind()
        for x, y in stones:
            uf.union(x, y + 10000)  # 用 y + 10000 是为了区分行和列
        return len(stones) - len({uf.find(x) for x, y in stones})

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x!=self.parent.setdefault(x, x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


        

