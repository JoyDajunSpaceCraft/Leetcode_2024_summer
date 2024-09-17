class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res = {}
        for i in s1.split(" "):
            if i not in res:
                res[i] = 1
            else:
               res[i]+=1
        for i in s2.split(" "):
            if i not in res:
                res[i] = 1
            else:
               res[i]+=1
        return_ = []
        for k,v in res.items():
            if v==1:
                return_.append(k)
        return return_