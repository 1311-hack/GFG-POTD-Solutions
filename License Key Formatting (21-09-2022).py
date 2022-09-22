class Solution:
    def ReFormatString(self,S, K):
        #code here
        l = S.split("-")
        s = "".join(l)
        s = s.upper()
        a = len(s)%K
        ans = ""
        for i in range(a):
            ans += s[i]
        count = 0
        for i in range(a,len(s)):
            if i != 0 and count%K == 0:
                ans += "-"
                ans += s[i]
            else:
                ans += s[i]
            count += 1
        return ans
