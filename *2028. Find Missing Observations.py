class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        cur_sum = sum(rolls)

        miss_sum = mean*(m+n) - cur_sum

        if miss_sum>6*n or miss_sum< n:
            return []
        result = [1]*n
        miss_sum -= n
        i = 0
        
        while i <n:
            add_val = min(5, miss_sum)
            result[i] +=add_val
            miss_sum -= add_val
            i+=1
        return result
