a = [1,2,3,4]
b = a
sum = 0
k = 7
for i in a:
    b.remove(i)
    for j in b:
        print(b)
        if sum == k:
            break
        sum+=j