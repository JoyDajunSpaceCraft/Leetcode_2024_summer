class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_final = []
        t_final = []
        for i in range(len(s)):
            if s[i] == "#":
                if len(s_final)>0:
                    s_final = s_final[:len(s_final)-1]
            else:
                s_final.append(s[i])
        for j in range(len(t)):
            if t[j] == "#":
                if len(t_final)>0:
                    t_final = t_final[:len(t_final)-1]
            else:
                t_final.append(t[j])
        print(s_final)
        print(t_final)
        if s_final!=t_final:
            return False
        return True
