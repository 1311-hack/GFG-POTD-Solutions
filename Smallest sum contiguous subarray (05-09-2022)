def smallestSumSubarray(self, A, N):
        #Your code here
        #kadane's algorithm
        summ = 10**7
        minv = 0
        for i in range(N):
            minv += A[i]
            if minv < summ:
                summ = minv
            if minv > 0:
                minv = 0
        return summ
