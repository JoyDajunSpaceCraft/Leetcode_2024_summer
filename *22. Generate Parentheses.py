class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s, left, right):
            if len(s)  == n*2:
                result.append(s)
                return 
            if left < n:
                backtrack(s+"(", left+1, right)
            if right < left:
                backtrack(s+")", left, right+1)
            
        
        result = []
        backtrack("", 0, 0)
        return result 