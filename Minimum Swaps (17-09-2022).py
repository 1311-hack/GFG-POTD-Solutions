from typing import List
class Solution:
    def minimumSwaps(self,c : List[int], v : List[int],n : int,k : int,b : int, t : int) -> int:
        # code here
        list1 = []
        minSwaps = 0
        for i in range(n):
            a = c[i]+v[i]*t
            if a >= b: list1.append(i)
        list1.sort(reverse=True)
        if len(list1) <  k: return -1
        list1 = list1[:k]
        for i in range(len(list1)):
            minSwaps += (n-list1[i]-i-1)
        return minSwaps
