class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        sorted_list = sorted(people, key=lambda x: (-x[0], x[1]))
        que = []
        for p in sorted_list:
            que.insert(p[1], p)
        return que