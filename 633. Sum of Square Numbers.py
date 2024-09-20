class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(math.sqrt(c))

        while a<=b:
            if a*a +b*b< c:
                a+=1
            elif a*a +b*b> c:
                b-=1
            else:
                return True
        return False