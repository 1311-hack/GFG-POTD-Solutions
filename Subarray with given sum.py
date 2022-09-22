#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s):
        #code here
        
        #variable to store current sum
        subSum = 0
        
        #start -> j, End -> i (for sliding window)
        i, j = 0, 0
        
        #lists to return for the given two conditions
        list1 = [0, 0]
        l = [-1]
        
        #boundary condition for value 0
        if s == 0:
            return l
        
        #sliding window
        while i <= n or j <= n:
            if subSum == s:
                list1[0] = j+1
                list1[1] = i
                return list1
            elif i == n and subSum < s:
                return l
            elif j == n and subSum > s:
                return l
            elif subSum > s:
                subSum -= arr[j]
                j += 1
            else:
                subSum += arr[i]
                i += 1
