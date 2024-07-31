class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        hash = [0]*26
        for i in words[0]:
            hash[ord(i)- ord("a")] +=1
        

        for num in range(1, len(words)):
            hashOther = [0]*26
            word = words[num]
            for i in word:
                hashOther[ord(i) - ord("a")] +=1
            for j in range(26):
                hash[j] = min(hash[j], hashOther[j])
        res = []
        for i in range(26):
            if hash[i]!=0:
                res.extend([chr(ord("a")+i)]*hash[i])
        return res