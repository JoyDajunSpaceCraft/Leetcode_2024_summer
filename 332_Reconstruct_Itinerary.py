# 为什么用 while？
# 定义一个递归函数dfs，从给定的起点开始构建行程。
# 在dfs函数中使用while循环，当start_pos在邻接表中且对应的终点列表不为空时，取出终点列表中的第一个终点（即按字典顺序的最小终点），并从邻接表中删除这个终点，然后对这个终点递归调用dfs。
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.adj = {}
        tickets.sort(key=lambda x:x[1])
        

        for k, v in tickets:
            if k in self.adj.keys():
                self.adj[k].append(v)
            else:
                self.adj[k] = [v]
        self.result = []
        self.dfs("JFK")
        return self.result[::-1]

    def dfs(self, start_pos):
        while start_pos in self.adj.keys() and len(self.adj[start_pos])>0:
            v = self.adj[start_pos][0]
            self.adj[start_pos].pop(0)
            self.dfs(v)
        self.result.append(start_pos)
