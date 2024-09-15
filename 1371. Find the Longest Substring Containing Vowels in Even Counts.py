class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mask = 0

        seen = {0:-1}
        vowels = {'a': 1 << 0, 'e': 1 << 1, 'i': 1 << 2, 'o': 1 << 3, 'u': 1 << 4}
        max_length = 0

        for i, char in enumerate(s):
            if char in vowels:
                mask ^= vowels[char]
            if mask in seen:
                max_length = max(max_length, i- seen[mask])
            else:
                seen[mask] = i
        return max_length