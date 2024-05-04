# https://leetcode.com/problems/boats-to-save-people/description/?envType=daily-question&envId=2024-05-04 
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people)-1
        boat=0
        while l<= r:
            if people[l] + people[r]<=limit:
                l+=1
            r-=1
            boat+=1
        return boat
# 这个问题的核心在于使用尽可能少的船将所有人运送过河。考虑到每条船可以承载两人，我们的策略应该尽量将重量较轻的人和重量较重的人配对，以确保每条船的载重接近极限值。

# 解决策略
# 排序：首先对人群按体重进行排序。
# 双指针技巧：设置两个指针，一个指向最轻的人（left），另一个指向最重的人（right）。
# 配对：
# 如果最轻的人和最重的人的体重和小于或等于限制，那么他们可以共乘一条船，然后移动两个指针（left 加一，right 减一）。
# 如果体重和超出限制，说明最重的人需要单独乘坐一条船，只移动 right 指针。
# 终止条件：当 left 指针超过 right 指针时，停止循环。
# 代码实现
# 接下来是 Python 代码实现这个策略：

# python
# Copy code
# def numRescueBoats(people, limit):
#     people.sort()  # 对人的体重进行排序
#     left, right = 0, len(people) - 1
#     boats = 0

#     while left <= right:
#         if people[left] + people[right] <= limit:
#             left += 1  # 最轻的和最重的一起走
#         right -= 1  # 最重的独自一船或者和最轻的一起走
#         boats += 1

#     return boats
# 示例运行
# 例如输入 people = [3, 2, 2, 1] 和 limit = 3，我们期望输出是 3，因为合理的安排是 [1, 2], [2], [3]。

# 这种方法的时间复杂度主要由排序决定，为 O(n log n)，其中 n 是人的数量。空间复杂度是 O(1)，只用了常数空间来存储指针和计数器。这样既优化了运行效率，也节约了空间。

# User
# 这里为什么都是  <=？
# ChatGPT
# 在这个问题中，使用 <= 是因为：

# people[left] + people[right] <= limit：这个条件检查最轻的人 (people[left]) 和最重的人 (people[right]) 的总重量是否不超过船的承载极限 (limit)。如果他们的总重量小于或等于限制，那么他们可以共同使用一条船。这里使用 <= 是因为包括了等于限制的情况，即刚好达到承载极限，也是允许的。
# while left <= right：这个循环条件确保 left 指针在 right 指针的左边或者与 right 指针相等时继续执行循环。如果 left 指针超过了 right 指针，说明所有可能的配对已经尝试过了。这里使用 <= 是为了确保 left 和 right 指向同一个人时，这个人也会被考虑到，即使他们需要独自一人乘船。
# 使用这两个 <= 条件是为了确保算法的全面性和准确性，覆盖所有可能的情况，包括边界条件。这样可以确保不会遗漏任何一个需要被救的人，并且尽可能减少所需的船只数量。






