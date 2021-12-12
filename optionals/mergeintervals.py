def mergeIntervals(a):
    a.sort
    result = []
    var = []
    def merger(a,b):
        return [a[0],b[1]]
    for i in range(len(a)):
        if(i+1==len(a)):
            break
        elif(a[i][1] >= a[i+1][0]):
            print(a[i][1] >= a[i+1][0])
            print(merger(a[i], a[i+1]))
            var = merger(a[i], a[i+1])
        else:
            result.append(var)
            var = []
        print(str(i) + str(a[i][1] >= a[i+1][0]))
    #result.remove([0,0])
    return result
print(mergeIntervals([[1,4],[4,5]]))