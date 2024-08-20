class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        min_left_idx = [0]*size
        min_right_idx = [0]*size

        result = 0
        min_left_idx[0] = -1

        for i in range(1, size):
            temp = i-1
            while temp>=0 and heights[temp] >= heights[i]:
                temp = min_left_idx[temp]
            min_left_idx[i] = temp

        min_right_idx[size-1] = size

        for i in range(size-2, -1, -1):
            temp = i+1
            while temp<size and heights[temp]>= heights[i]:
                # print(min_right_idx)
                temp = min_right_idx[temp]
            min_right_idx[i] = temp
        
        for i in range(size):
            area = heights[i] * (min_right_idx[i] - min_left_idx[i] - 1)
            result = max(area, result)
        
        return result


