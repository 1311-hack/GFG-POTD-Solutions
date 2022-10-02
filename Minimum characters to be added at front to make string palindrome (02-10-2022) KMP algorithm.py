#o(n) solution
class Solution:
    def minChar(self,str):
        #Write your code here
        n = len(str)
        revStr = str[::-1]
        newStr = str + "&" + revStr
        lps = lpsArray(newStr)
        return (n - lps[-1])

def lpsArray(str):
    m = len(str)
    length = 0
    lps = [None]*m
    lps[0] = 0
    i = 1
    while i < m:
        if str[length] == str[i]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                length = 0
                lps[i] = 0
                i += 1
    return lps
