class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        cur_sum = 0
        min_fuel = float("inf")
        for i in range(len(gas)):
            rest = gas[i] -cost[i]
            cur_sum += rest
            if cur_sum <min_fuel:
                min_fuel = cur_sum
        if cur_sum<0:
            return -1
        if min_fuel >=0:
            return 0
        
        for i in range(len(gas)-1, -1, -1):
            rest = gas[i] - cost[i]
            min_fuel+=rest
            if min_fuel >=0:
                return i
            
        return -1