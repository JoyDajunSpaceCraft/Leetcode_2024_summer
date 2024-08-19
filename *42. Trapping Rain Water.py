# class Solution:
#     def trap(self, height: List[int]) -> int:
#         leftheight, rightheight = [0]*len(height), [0]*len(height)

#         leftheight[0]=height[0]
#         for i in range(1,len(height)):
#             leftheight[i]=max(leftheight[i-1],height[i])
#         rightheight[-1]=height[-1]
#         for i in range(len(height)-2,-1,-1):
#             rightheight[i]=max(rightheight[i+1],height[i])

#         result = 0
#         for i in range(0,len(height)):
#             summ = min(leftheight[i],rightheight[i])-height[i]
#             result += summ
#         return result
class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]*len(height)
        right = [0]*len(height)

        left[0] = height[0]
        for i in range(1, len(height)):
            left[i] = max(height[i], left[i-1])
        right[-1] = height[-1]
        # print(right)
        for i in range(len(height)-2, -1, -1):
            right[i] = max(height[i], right[i+1])
            # print(right)
        result = 0
        for i in range(len(height)):
            res = min(left[i], right[i]) - height[i]
            # if res>0:
            result+=res
        return result 


# #         left = 0
# #         right = 0
# #         count = 0
# #         for i in range(len(height)):
# #             if i==0 or i == len(height)-1: 
# #                 continue

# #             left = height[i-1]
# #             right = height[i+1]
# #             for j in range(i-1):
# #                 if left < height[j]:
# #                     left = height[j]
# #             for k in range(i+2, len(height)):
# #                 if right < height[k]:
# #                     right = height[k]
# #             res = min(left, right) - height[i]
# #             if res>0:
# #                 count+=res
# #         return count
