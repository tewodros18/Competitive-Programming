for i in range(len(testcase)):
    if(testcase[i] == target):
        right = (len(testcase) - 1) - i
        left = i
        if(left%2 == 0 and right%2 == 0):
            print("YES")
            return
print("No")
