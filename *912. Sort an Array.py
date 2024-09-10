def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left_half = merge_sort(nums[:mid])
    right_half = merge_sort(nums[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    
    # 将剩余的元素加进去
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    
    return sorted_array
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)

    def merge(self, left, right):
        sort_ = []
        i = 0
        j = 0


        while i<len(left) and j<len(right):
            if left[i]< right[j]:
                sort_.append(left[i])
                i+=1
            else:
                sort_.append(right[j])
                j+=1
        sort_.extend(left[i:])
        sort_.extend(right[j:]) 
        return sort_


        
    def merge_sort(self,nums):
        if len(nums)<=1:
            return nums
        mid =len(nums)//2
        left_half = self.merge_sort(nums[:mid])
        right_half= self.merge_sort(nums[mid:])
        return self.merge(left_half,right_half)
