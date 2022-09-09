#function to count and return the number of palindromic subsequences.
#using dynamic programming DP in Python.
    def countPS(self,string):
        # Code here
        dp = [[0 for _ in range(len(string))] for _ in range(len(string))]
        i, j, q = 0, 0, 0
        g = 1
        while (i < len(string) and j < len(string)):
            dp[i][j] = 1
            i += 1
            j += 1
        while (g < len(string)):
            p = g
            q = 0
            while (p < len(string) and q < len(string)):
                if (string[p] == string[q]):
                    dp[q][p] = dp[q][p-1] + dp[q+1][p] + 1
                else:
                    dp[q][p] = dp[q][p-1] + dp[q+1][p] - dp[q+1][p-1]
                p += 1
                q += 1
            g += 1
        ans = (dp[0][len(string) - 1] % 1000000007)
        return ans
