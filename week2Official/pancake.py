def pancakeSort(arr):
        left = 0
        right = len(arr) - 1
        flip = []
        while(right>0):
            if(left == right):
                right-=1
                left=0
            if(arr[left] > arr[right]):
                if(left==0):
                    arr = arr[:right+1][::-1] + arr[right+1:]
                    flip.append(right+1)
                else:
                    arr = arr[:left+1][::-1] + arr[left+1:]
                    flip.append(left+1)
                left = 0
            elif(arr[left] < arr[right]):
                left+=1
        return flip
print(pancakeSort([1,2,3]))