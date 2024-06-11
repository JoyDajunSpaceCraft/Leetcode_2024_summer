class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        str_n = str(n)
        strNum = list(str(n))
        for i in range(len(strNum)-1, 0, -1):

            if int(strNum[i-1])>int(strNum[i]):
                strNum[i-1] = str(int(strNum[i-1])-1)
                for j in range(i, len(strNum)):
                    strNum[j] = '9'

        return int(''.join(strNum))

