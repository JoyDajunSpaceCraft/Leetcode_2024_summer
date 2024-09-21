class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        def dfs(curr):
            if curr>n:
                return 
            result.append(curr)

            for i in range(10):
                if curr *10 + i > n:
                    break
                dfs(curr *10 + i)
        for i in range(1, 10):
            dfs(i)
        return result

                
    