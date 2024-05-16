# https://leetcode.com/problems/k-closest-points-to-origin/?envType=problem-list-v2&envId=rwz9zas3
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        max_heap = []
        for item in points:
            dist = item[0]**2 + item[1]**2
            new_item = (dist, item)
            heappush(max_heap,new_item)
        print(max_heap)
        for i in range(0, k):
            result.append(heappop(max_heap)[1])
        return result