def insertionsort(a):
    output = ""
    for i in range(1,len(a)):
        value = a[i]
        hole = i
        while( hole>0 and (a[hole-1] > value)):
            a[hole]  = a[hole-1]
            hole-=1
            print(' '.join([str(elem) for elem in a]))
        a[hole] = value
    print(' '.join([str(elem) for elem in a]))

insertionsort([1,2,4,5,3])