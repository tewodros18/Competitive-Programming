import heapq
testcases = input().split()
for i in range(len(testcases)):
    testcases[i] = int(testcases[i])
questions = input().split()
#heap = []
for i in range(len(questions)):
    questions[i] = int(questions[i])
    #heapq.heappush(heap,questions[i])
tests = []
for i in range(testcases[0]):
    tests.append(int(input()))
questions.sort()
def check(test):
    left = 0 
    right = len(questions) - 1
    if(test > questions[-1]):
        print("NO")
        return
    if(test < questions[0]):
        print("NO")
        return 
    while(left <= right):
        mid = (left + right) //2
        if(questions[mid] == test):
            if(len(questions) - mid == len(questions)):
                print("NO")
                return
            if(len(questions) - mid >= len(questions)//2 + 1):
                print("YES")
                return
            else:
                print("NO")
                return
        elif(questions[mid] > test):
            right = mid - 1
        else:
            left = mid + 1
    if(len(questions) - mid == len(questions)):
        print("NO")
        return
    if(len(questions) - mid >= len(questions)//2 + 1):
        print("YES")
        return
    else:
        print("NO")
        return
    
for i in tests:
    check(i)
        

-