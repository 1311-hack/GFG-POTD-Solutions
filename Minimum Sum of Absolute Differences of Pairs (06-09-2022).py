#Function to find Minimum Sum of Absolute Differences of Pairs.

def findMinSum(self, A,B,N):
        A.sort()
        B.sort()
        minsum = 0
        for i in range(N):
            minsum += abs(A[i] - B[i])
        return minsum
