a = input().split()
problems = int(a[0])
traveltime = int(a[1])
left = 1 
right = problems
def slove(problem):
    lst = [5*i for i in range(1,problem+1)]
    sm = sum(lst)
    return sum
while(left <= right):
    mid = (left + right)//2
    Sums = slove(mid)
    paryt = Sums + traveltime + 1200
    if(party > 1440):
        right = mid - 1
    else:
        left = mid + 1
print(left)