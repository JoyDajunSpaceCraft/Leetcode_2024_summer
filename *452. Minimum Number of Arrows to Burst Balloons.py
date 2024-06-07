class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0: return 0
        points.sort(key = lambda x:x[0])
        count = 1
        sl, sr = points[0][0], points[0][1]

        for i in points:
            if i[0]>sr:
                count+=1
                # sl, sr = i[0], i[1]
                sr = i[1]
            else:
                # sl = min(i[0], sl)
                sr = min(i[1], sr)
        return count
