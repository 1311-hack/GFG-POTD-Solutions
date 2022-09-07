#Explanation is given after the code.
#Time complexity O(N).
#Copy the function and use it to run all the test cases.
def isStackPermutation(self, N : int, A : List[int], B : List[int]) -> int:
        # code here
        res = 0
        i = 0
        j = 0
        stack = [200001]
        while (i <= N and j < N):
            if stack[-1] == B[j]:
                stack.pop()
                j += 1
            elif (i < N):
                stack.append(A[i])
                i += 1
            else:
                i += 1
        if stack[-1] == 200001:
            return 1
        else:
            return 0            



#test cases (main function):
if __name__ == '__main__':
    test_cases = int(input())
    while test_cases > 0:
        N = int(input())
        A = [int(x) for x in input().strip().split()]
        B = [int(x) for x in input().strip().split()]
        print(isStackPermutation(N, A, B))
        test_cases -= 1
        
