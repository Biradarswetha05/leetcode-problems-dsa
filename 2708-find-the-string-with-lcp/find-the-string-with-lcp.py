class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n=len(lcp)
        for i in range(n):
            if lcp[i][i]!=n-i:return""
            for j in range(n):
                if lcp[i][j]!=lcp[j][i]:return""
        p=list(range(n))
        def f(x):
            if p[x]!=x:p[x]=f(p[x])
            return p[x]
        def u(x,y):p[f(x)]=f(y)
        for i in range(n):
            for j in range(i+1,n):
                if lcp[i][j]>0:u(i,j)
        g={}
        c=97
        w=[""]*n
        for i in range(n):
            r=f(i)
            if r not in g:
                if c>122:return""
                g[r]=chr(c);c+=1
            w[i]=g[r]
        w="".join(w)
        dp=[[0]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if w[i]==w[j]:
                    dp[i][j]=1+(dp[i+1][j+1] if i+1<n and j+1<n else 0)
        return w if dp==lcp else""