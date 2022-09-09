def findMinTime(self, n : int, l : int, arr : List[int]) -> int:
        # code here
        arr.sort()
        low = arr[0]
        high = int(arr[l-1]*((n*(n+1))/2))
        time = 0
        while (low<=high):
            mid = int(low+(high-low)/2)
            if possible(mid,arr,n) == 1:
                time = mid
                high = mid - 1
            else:
                low = mid + 1
        return time
def possible(mid,arr,n):
    donuts = 0
    for i in arr:
        timeTaken = 0
        timeWillTake = i
        time = timeTaken + timeWillTake
        while (time <= mid):
            donuts += 1
            timeWillTake += i
            time += timeWillTake
    if donuts >= n:
        return 1
    else:
        return 0

