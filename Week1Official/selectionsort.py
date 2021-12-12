class Solution: 
    def select(self, arr, i):
        # code here 
        minimum = i-1
        for j in range(i,len(arr)):
            if arr[minimum] > arr[j]:
                minimum = j
        return minimum
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)-1):
            minimum = i
            minimum = select(arr,i+1)
            (arr[i],arr[minimum])=(arr[minimum],arr[i])

        return arr