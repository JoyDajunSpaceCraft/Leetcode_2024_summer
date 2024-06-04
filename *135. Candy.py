class Solution:
    def candy(self, ratings: List[int]) -> int:
        cand_v = [1]*len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                cand_v[i]=cand_v[i-1]+1
        
        for i in range(len(ratings) -2, -1,-1):
            if ratings[i+1] <ratings[i]:
                cand_v[i] = max(cand_v[i], cand_v[i+1]+1)
        return sum(cand_v)
