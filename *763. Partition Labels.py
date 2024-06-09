class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_oc = {}
        for i, ch in enumerate(s):
            last_oc[ch] = i

        start = 0
        end = 0
        result = []

        for i, ch in enumerate(s):
            end = max(end, last_oc[ch])
            if end == i:
                result.append(end-start+1)
                start = i+1
        return result
