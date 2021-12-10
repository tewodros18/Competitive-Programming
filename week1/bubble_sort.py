def BubbleSort(A_list):
    length_of_list = len(A_list)
    while(True):
        swapped = False
        for i in range(1,length_of_list):
            if(A_list[i-1] > A_list[i]):
                (A_list[i-1],A_list[i]) = (A_list[i],A_list[i-1])
                swapped = True
        if(not swapped):
            break
    print(A_list)          
    return
BubbleSort([2,0,1,0,1,2,1,3])
