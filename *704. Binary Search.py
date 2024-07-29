class Solution:
    def search(self, nums: List[int], target: int) -> int:
        le = 0
        right = len(nums)-1

        while le<=right:
            mid = le+(right-le)//2
            if nums[mid]> target:
                right = mid-1
            elif nums[mid]<target:
                le = mid+1
            else:
                return mid
        return -1