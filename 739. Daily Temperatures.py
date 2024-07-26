class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]* len(temperatures)
        stack = [0]

        for i in range(1, len(temperatures)):
            if temperatures[i] <=temperatures[stack[-1]]:
                stack.append(i)
            else:
                while len(stack)!=0 and temperatures[i]>temperatures[stack[-1]]:
                    answer[stack[-1]] = i- stack[-1] # 在 while 循环中，每弹出一个栈顶索引，计算 answer 对应位置的值，即从当前索引减去弹出栈顶索引的值，这就是从栈顶元素对应的温度到当前温度的天数差。
                    stack.pop()
                stack.append(i)
        return answer
