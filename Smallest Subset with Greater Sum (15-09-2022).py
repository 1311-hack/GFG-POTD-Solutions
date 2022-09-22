class Solution:
    def minSubset(self, A,N):
        A.sort(reverse=True)
        all_sum = sum(A)
        upsum, count = 0, 0
        for i in range(N):
            all_sum -= A[i]
            upsum += A[i]
            count += 1
            if upsum > all_sum:
                break
        return count
