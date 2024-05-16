# 242. Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        a_count = Counter(s)
        b_count = Counter(t)
        print(b_count)
        return a_count == b_count