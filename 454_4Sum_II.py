# https://leetcode.com/problems/4sum-ii/
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hash_map = dict()
        for n1 in nums1:
            for n2 in nums2:
                if n1+n2 in hash_map.keys():
                    hash_map[n1+n2]+=1
                else:
                    hash_map[n1+n2]=1
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                key = -n4-n3
                if key in hash_map.keys():
                    count+=hash_map[key]
        return count 
