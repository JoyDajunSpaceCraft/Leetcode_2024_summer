class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n!= len(original):
            return []
        # m is row , n is col
        new_rew = []
        for i in range(m):
            res = original[i*n:(i+1)*n]
            new_rew.append(res)
            # print(res)
        return new_rew
