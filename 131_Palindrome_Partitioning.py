# https://programmercarl.com/0131.%E5%88%86%E5%89%B2%E5%9B%9E%E6%96%87%E4%B8%B2.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.backtracking(s, 0, [], result)
        return result

    def backtracking(self, s, startIndex, path, result):
        if startIndex == len(s):
            result.append(path[:])
            return 

        for i in range(startIndex, len(s)):
            if s[startIndex: i+1] == s[startIndex: i+1][::-1]:
                path.append(s[startIndex:i+1])
                self.backtracking(s, i+1, path, result)
                path.pop()
            