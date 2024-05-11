# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/?envType=daily-question&envId=2024-05-11

# 在你的代码中，你使用了 heapq 来管理一组工人的质量值，但你对 heapq 进行了负数处理，即通过 -ratio[i][1] 来添加元素。这实际上是在使用 heapq（默认是最小堆）来模拟一个最大堆。通过插入元素的负值，你可以保证堆顶（即 Python 中 heapq 管理的最小值）是原始数据中的最大值的负数。因此，当你调用 heapq.heappop(max_heap) 时，你实际上是在移除当前质量最高的工人（因为你存储的是负值，最小的负数对应最大的正数）。

# 这个策略在你的问题中非常关键，因为算法需要维持一个固定大小为 k 的工人组，并且在探索所有可能的组合时始终保持总成本最低。下面是你代码中使用最大堆（通过模拟）的原因和逻辑解释：

# 初始化阶段：你首先排序工人的比例（wage/quality），然后遍历前 k 个工人，把他们放入最大堆中（实际上存储的是他们质量的负值）。这时，你计算出当前这个组合的成本。
# 替换和计算最小成本：当你继续遍历剩下的工人时（从第 k 个开始），你会试图通过替换掉当前最大堆中“质量最高”的工人（实际上是堆顶的元素，即最小的负数，对应最大的质量），用当前工人的质量来替代，来看是否能降低整体的支付成本。通过这种方式，你每次都保持了组中有 k 个工人，同时尝试最小化基于当前比例的总成本。
# 更新成本：如果通过替换可以得到更低的成本，你将更新结果。
# 这种方法的关键是始终通过维持一个大小为 k 的最大堆（存储质量的负值）来控制总成本，并通过适时替换堆中成本最高（质量最大）的工人来尝试降低成本。


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        #  By default, sorted sorts tuples first by the first element, and if the first elements are the same, then by the second element.
        ratio = sorted([(w/q, q) for w, q in zip(wage, quality)])
        max_heap = []
        quality_sum = 0
        max_ratio = 0.0

        for i in range(k):
            max_ratio = max(max_ratio, ratio[i][0])
            quality_sum += ratio[i][1]
            heapq.heappush(max_heap, -ratio[i][1])
        res = max_ratio* quality_sum

        for i in range(k, len(quality)):
            max_ratio = max(max_ratio, ratio[i][0])
            quality_sum += ratio[i][1] + heapq.heappop(max_heap)
            heapq.heappush(max_heap, -ratio[i][1])
            res = min(res, max_ratio* quality_sum)
        return res