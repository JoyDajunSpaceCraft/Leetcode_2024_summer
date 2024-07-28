class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def getRight(nums, target):
            left = 0
            right = len(nums)-1
            rightboard = -2
            while left<= right:
                mid = left+(right-left)//2
                if nums[mid]>target:
                    right = mid-1
                else:
                    left =mid+1
                    rightboard = left 
            return rightboard
        def getLeft(nums, target):
            left = 0
            right = len(nums)-1
            leftboard = -2
            while left <= right:
                mid = left+(right-left)//2
                if nums[mid]>=target:
                    right = mid-1
                    leftboard = right 
                else:
                    left =mid+1
                   
            return leftboard
        leftboard = getLeft(nums, target)
        rightboard = getRight(nums, target)


        if leftboard==-2 or rightboard==-2:
            return [-1, -1]
        if rightboard - leftboard >1:
            return [leftboard+1, rightboard-1]
        return [-1, -1]