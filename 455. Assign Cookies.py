class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort() # child
        s.sort() # food
        index = 0
        for i in range(len(s)):
            if index<len(g) and g[index]<= s[i]:
                index+=1
        return index 
            