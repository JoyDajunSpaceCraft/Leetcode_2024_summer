# https://leetcode.com/problems/k-th-smallest-prime-fraction/description/?envType=daily-question&envId=2024-05-10
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        min_heap = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                fraction = (arr[i]/arr[j], (arr[i], arr[j]))
                heappush(min_heap, fraction)
        for _ in range(k-1):
            heappop(min_heap)
        return heappop(min_heap)[1]

