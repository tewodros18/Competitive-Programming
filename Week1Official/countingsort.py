def countingSort(arr):
    countbits = [0] * (100)
    for i in arr:
        countbits[i]+=1
    return countbits
print(countingSort([1,1,3,2,1]))      