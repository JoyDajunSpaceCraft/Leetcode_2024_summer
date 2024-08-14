class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # 创建一个布尔列表，表示每个数字是否为素数，初始时所有数字都标记为True
        is_prime = [True] * n
        
        # 从2开始，逐步筛选出素数
        i = 2
        while i * i < n:
            if is_prime[i]:
                # 标记所有 i 的倍数为非素数
                for j in range(i * i, n, i):
                    is_prime[j] = False
            i += 1
        
        # 统计标记为True的数量，但需减去0和1，因为它们不是素数
        return sum(is_prime) - is_prime[0] - is_prime[1]
