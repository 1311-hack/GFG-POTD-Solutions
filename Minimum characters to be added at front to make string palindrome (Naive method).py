class Solution:
    def minChar(self,str):
        #Write your code here
        n = len(str)
        if n%2 == 0:
            a = (n//2) - 1
        else:
            a = (n+1)//2 - 1
        for i in range(a, -1, -1):
            p = str[:i]
            q = str[i+i:i:-1]
            p2 = str[:i+1]
            q2 = str[i+i+1:i:-1]
            if p2 == q2:
                r = n - ((i*2) + 2)
                return r
            if p == q:
                r = n - ((i*2) + 1)
                return r
        r = n - 1
        return r
