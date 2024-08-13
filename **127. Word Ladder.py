class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        queue = deque([beginWord])
        mapping = {beginWord:1}
        while queue:
            print(queue)
            word = queue.popleft()
            
            path = mapping[word]
            for i in range(len(word)):
                word_list = list(word)
                for j in range(26):
                    word_list[i] = chr(ord('a')+j)
                    new_word = "".join(word_list)
                    if new_word == endWord:
                        path+=1
                        return path
                    if new_word in wordList and new_word not in mapping:
                    # if new_word in wordList:
                        mapping[new_word] = path+1
                        queue.append(new_word)
        
        return 0
