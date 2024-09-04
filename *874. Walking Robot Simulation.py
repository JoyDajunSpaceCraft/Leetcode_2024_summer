class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (0, -1), (-1, 0)]

        obstacle_set = set(map(tuple, obstacles))
        x, y = 0,0
        max_distance =0
        direct_idx = 0

        for command in commands:
            if command==-1:
                direct_idx = (direct_idx+1)%4
            elif command == -2:
                direct_idx = (direct_idx-1)%4
            else:
                dx, dy = directions[direct_idx]
                for i in range(command):
                    if (dx+x, dy+y) not in obstacle_set:
                        x+=dx
                        y+=dy
                        max_distance = max(max_distance, x*x+y*y)
                    else:
                        break
        return max_distance
