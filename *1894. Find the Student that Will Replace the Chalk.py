class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalk = sum(chalk)
        k %= total_chalk

        for i, ck in enumerate(chalk):
            if k<ck:
                return i
            k-=ck

