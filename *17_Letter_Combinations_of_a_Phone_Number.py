# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
class Solution:
    def __init__(self):
        self.letterMap = [
            "",     # 0
            "",     # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs", # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]
        self.result = []
        self.s = ""
    
    def backtracking(self, digists, index):
        if len(digists) == index:
            self.result.append(self.s)
            return 
        int_ = int(digists[index])
        strings =self.letterMap[int_]
        for i in strings:
            self.s+=i
            index+=1
            self.backtracking(digists, index)
            index-=1
            self.s = self.s[:-1]

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return self.result
        self.backtracking(digits, 0)
        return self.result

