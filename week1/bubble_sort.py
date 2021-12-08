def BubbleSort(A_list):
    length_of_list = len(A_list)
    while(True):
        swapped = False
        for i in range(1,length_of_list-1):
            if(A_list[i-1] > A_list[i]):
                (A_list[i-1],A_list[i]) = (A_list[i],A_list[i-1])
                swapped = True
        if(not swapped):
            break
    print(A_list)          
    return

