# https://leetcode.com/problems/maximize-happiness-of-selected-children/description/?envType=daily-question&envId=2024-05-09
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0
        i = 0
        while k>0:
            happiness[i] = max(happiness[i]-i, 0)
            res += happiness[i]
            i+=1
            k-=1
        return res