class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        res = ['?'] * (n + m - 1)
        fixed = [False] * (n + m - 1)
        
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if res[i + j] == '?' or res[i + j] == str2[j]:
                        res[i + j] = str2[j]
                        fixed[i + j] = True
                    else:
                        return ""
        
        for i in range(len(res)):
            if res[i] == '?':
                res[i] = 'a'
        
        for i in range(n):
            if str1[i] == 'F':
                if ''.join(res[i:i + m]) == str2:
                    changed = False
                    for j in range(m - 1, -1, -1):
                        idx = i + j
                        if not fixed[idx]:
                            for c in 'abcdefghijklmnopqrstuvwxyz':
                                if c != str2[j]:
                                    res[idx] = c
                                    changed = True
                                    break
                        if changed:
                            break
                    if not changed:
                        return ""
        
        return ''.join(res)