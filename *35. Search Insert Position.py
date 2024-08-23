class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left<= right: # [left, right]
            mid = (left + right) // 2
            print(mid)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid]>target:
                right = mid-1
            else:
                return mid
        return left
        # left, right = 0, len(nums) - 1

        # while left <= right:
        #     middle = (left + right) // 2

        #     if nums[middle] < target:
        #         left = middle + 1
        #     elif nums[middle] > target:
        #         right = middle - 1
        #     else:
        #         return middle
        # return right + 1
