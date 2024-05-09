# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# 代码结构和初始化
# Solution 类包含了 findSubstring 方法，用来实现问题的求解。
# length 存储每个单词的长度（由于题目规定，words 中所有单词长度相同）。
# word_count 是一个计数器（Counter），用来统计 words 中每个单词的出现次数。
# indexes 是一个列表，用于存储满足条件的子串的起始索引。
# 滑动窗口算法
# 外层循环：for i in range(length)，这里 i 从 0 到单词长度-1，对应于字符串 s 中的所有可能的起始位置（对于给定单词长度的所有偏移）。
# 内层循环：for j in range(i, len(s) - length + 1, length)，j 从 i 开始，每次增加一个单词的长度 length，以检查所有可能的单词在 s 中的位置。
# 窗口内部逻辑
# 每次循环，从 s 中截取出当前长度为 length 的单词 word。
# 如果 word 不在 word_count 中，说明它不是要找的单词，重置 start 为 j + length（跳过当前单词），并清空 window 和 words_used。
# 如果 word 是目标单词之一，则增加窗口中该单词的计数，并更新 words_used。
# 如果窗口中某个单词的数量超过了它在 word_count 中的数量，从窗口的开始位置 start 向右移动，直到该单词的数量不超过应有的数量。
# 如果窗口中使用的单词总数等于 words 的长度，将 start 加入到 indexes 中。
# 性能说明
# 时间复杂度为 O(n * k)，其中 n 是字符串 s 的长度，k 是每个单词的长度。
# 空间复杂度为 O(m * k)，其中 m 是单词数组 words 的长度，k 是每个单词的长度。
# 行 window[word] > word_count[word]
# 这行代码检查当前窗口中的某个单词 word 的数量是否超过了它在 words 列表中应有的数量。如果是，表示当前窗口不可能是一个有效的连接字符串，因为它包含了太多的某个单词。

# 行 window[s[start:start + length]] -= 1
# 如果发现某个单词的数量超标，我们需要调整窗口。这行代码实际上是从窗口中减去窗口开始处的单词。s[start:start + length] 表示的是窗口当前开始位置的单词，通过减去这个单词的计数，我们相当于是在缩小窗口的左边界，移除了窗口开始的第一个单词。

# 行 start += length
# 这行代码将窗口的起始位置向右移动一个单词的长度。这意味着我们正在尝试一个新的子串作为可能的解，因为之前的窗口因为某个单词超标而被判定为无效。

# 行 words_used -= 1
# 由于我们移除了窗口开始的单词，所以用于跟踪当前窗口中单词总数的计数器 words_used 需要减少1，以反映我们现在窗口中有一个单词被移出了。

# 操作结果
# 通过这些操作，代码有效地调整了窗口的大小和位置，以确保所有在 words 列表中的单词在窗口中的数量都不会超过他们应有的数量。这样一来，只有当窗口中的单词完全匹配 words 中的单词（包括数量和种类）时，我们才会将窗口的起始位置 start 添加到结果列表 indexes 中。
from collections import Counter, defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        length = len(words[0])
        word_count = Counter(words)
        indexes = []

        for i in range(length):
            start = i
            window = defaultdict(int)
            words_used = 0

            for j in range(i, len(s) - length + 1, length):
                word = s[j:j+length]

                if word not in word_count:
                    start = j +length
                    window = defaultdict(int)
                    words_used = 0
                    continue
                
                words_used +=1
                window[word] +=1

                while window[word] > word_count[word]:
                    window[s[start:start + length]] -= 1
                    start += length
                    words_used -= 1
                if words_used == len(words):
                    indexes.append(start)
        return indexes

            