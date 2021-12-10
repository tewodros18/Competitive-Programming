def bubblesort(toSort):
    swaps = 0
    for i in range(0,len(toSort)):
        for j in range(0,len(toSort)-1):
            if (toSort[j] > toSort[j+1]):
                swaps+=1
                (toSort[j],toSort[j+1]) = (toSort[j+1],toSort[j])
    return [swaps,toSort[0],toSort[-1]]
print(bubblesort([2,0,1,0,1,2]))