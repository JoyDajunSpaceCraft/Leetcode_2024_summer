class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_layer(prefix, n):
            cur = prefix
            next_prefix = cur+1
            step = 0
            while cur<=n:
                step += min(n+1, next_prefix) - cur
                cur*=10
                next_prefix *=10
            return step
        current = 1
        k-=1
        while k> 0:
            step = count_layer(current, n)
            if step <= k:
                current+=1
                k-=step
            else:
                current*=10
                k-=1
        return current 

            