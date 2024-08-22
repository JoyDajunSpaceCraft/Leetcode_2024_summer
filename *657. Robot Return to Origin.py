class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        x = 0
        y = 0
        for i in range(len(moves)):
            item  = moves[i]
            if item == "L":
                x-=1
            elif item=="D":
                y-=1
            elif item=="U":
                y+=1
            elif item=="R":
                x+=1
            # print(x)
            # print(y)
        if x==0 and y==0:
            return True
        return False 