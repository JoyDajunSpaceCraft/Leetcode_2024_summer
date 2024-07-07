from collections import deque

class MyQueue:
    def __init__(self):
        self.queue = deque() 
    def pop(self, value):
        if self.queue and self.queue[0]==value:
            self.queue.popleft()
        
    def push(self, value):
        while self.queue and self.queue[-1]< value:
            self.queue.pop()
        self.queue.append(value)

    def front(self):
        return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = MyQueue()
        for i in range(k):
            que.push(nums[i])
        result = []
        result.append(que.front())

        for i in range(k, len(nums)):
            que.pop(nums[i-k])
            que.push(nums[i])
            result.append(que.front())
        return result