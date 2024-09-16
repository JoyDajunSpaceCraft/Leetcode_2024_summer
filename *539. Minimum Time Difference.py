class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def timeToMinutes(time):
            hour, minut = map(int, time.split(":"))
            return hour*60 + minut
        
        minutes = sorted([timeToMinutes(time) for time in timePoints])
        min_diff = float('inf')

        for i in range(1, len(timePoints)):
            print("minutes[i]", minutes[i])
            print("minutes[i-1]",minutes[i-1])
            min_diff = min(min_diff, minutes[i] - minutes[i-1])
        print("min_diff 1", min_diff)
        min_diff = min(min_diff, 1440 - (minutes[-1] - minutes[0]))
        print("min_diff 2 ", min_diff)
        return min_diff
        