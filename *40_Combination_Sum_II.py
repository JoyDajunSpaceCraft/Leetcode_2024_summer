# https://leetcode.com/problems/combination-sum-ii/description/
  # https://programmercarl.com/0040.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CII.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        used = [False] * len(candidates)
        result = []
        candidates.sort()
        total = 0
        startIndex = 0
        path = []
        self.backtracking(candidates, target, total, startIndex, used, path, result)
        return result

    def backtracking(self, candidates, target, total, startIndex, used, path, result):
        # path is the current option
        if total==target:
            result.append(path[:])
        for i in range(startIndex, len(candidates)):
            if i > startIndex and candidates[i] == candidates[i-1] and not used[i-1]:
                continue
            if total+ candidates[i]>target:
                break

            used[i] = True
            path.append(candidates[i])
            total += candidates[i]
            self.backtracking(candidates, target, total, i+1, used,path ,result)
            used[i] = False
            total-=candidates[i]
            path.pop()




  