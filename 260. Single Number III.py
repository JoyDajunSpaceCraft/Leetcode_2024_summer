class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorResult = 0
        for num in nums:
            xorResult ^= num
        
        # 第二步：找到异或结果中的最低有效位为1的位
        diffBit = xorResult & (-xorResult)
        
        # 第三步：根据这个位将数字分成两组，分别进行异或操作
        num1, num2 = 0, 0
        for num in nums:
            if num & diffBit:
                num1 ^= num
            else:
                num2 ^= num
        
        return [num1, num2]