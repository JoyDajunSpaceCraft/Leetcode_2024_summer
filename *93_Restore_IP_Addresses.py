# https://programmercarl.com/0093.%E5%A4%8D%E5%8E%9FIP%E5%9C%B0%E5%9D%80.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        results = []
        self.backtracking(s, 0, [], results)
        return results  

    def backtracking(self, s, index, path, results):
        if index==len(s) and len(path)==4:
            results.append(".".join(path))
            return 

        if len(path)> 4:
            return
        
        for i in range(index, min(index+3, len(s))):
            if self.is_valid(s, index, i):
                sub = s[index: i+1]
                path.append(sub)
                self.backtracking(s, i+1, path, results)
                path.pop() 
    
    def is_valid(self, s, start, end):
        if start>end:
            return False
        if s[start]=="0"and start != end: 
            return False
        print("s[start:end+1]",s[start:end+1])
        return 0<=int(s[start:end+1])<=255
    # def is_valid(self, s, start, end):
    #     if start > end:
    #         return False
    #     if s[start] == '0' and start != end:  # 0开头的数字不合法
    #         return False
    #     num = int(s[start:end+1])
    #     return 0 <= num <= 255