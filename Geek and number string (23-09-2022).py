class Solution:
    def minLength(self, s, n): 
        #code here 
        S = []
        stack = []
        i = 1
        for j in s:
            S.append(int(j))
        stack.append(S[0])
        while i < n:
            stack.append(S[i])
            if len(stack)>1 and (stack[-2]-1) == S[i] and S[i]%2!=0:
                stack.pop()
                stack.pop()
                i += 1
            elif len(stack)>1 and (stack[-2]+1) == S[i] and S[i]%2==0:
                stack.pop()
                stack.pop()
                i += 1
            elif len(stack)>1 and stack[-2]+stack[-1]==9 and (stack[-2]==9 or stack[-2]==0):
                stack.pop()
                stack.pop()
                i += 1
            else:
                i += 1
        return len(stack)
