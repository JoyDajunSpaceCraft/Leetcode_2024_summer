class Solution:
    def balancedStringSplit(self, s: str) -> int:
        diff  = 0
        res = 0
        for i in s:
            if i == "L":
                diff-=1
            else:
                diff+=1
            if diff==0:
                res+=1
        return res