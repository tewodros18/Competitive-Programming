def select(arr, i):
    # code here 
    return min(arr)
def selectionSort(arr,n):        
    #code here
    for i in range(len(arr)):
        value = arr.index(select(arr[i:],i))
        (arr[i],arr[value]) = (arr[value],arr[i])
    return arr
print(selectionSort([4,1,3,9,7], 5))