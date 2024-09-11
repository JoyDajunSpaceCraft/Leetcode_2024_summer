class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d = {}
        res = []

        desScore = sorted(score, reverse=True)
        print(desScore)
        for i in range(len(desScore)):
            if i==0:
                d[desScore[i]] = "Gold Medal"
            elif i == 1:
                d[desScore[i]] ="Silver Medal"
            elif i==2:
                d[desScore[i]] ="Bronze Medal"
            else:
                d[desScore[i]] = str(i+1)
        print(d)
        for i in range(len(score)):
            res.append(d[score[i]])
        return res
