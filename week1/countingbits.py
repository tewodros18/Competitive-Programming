def count(n):
    "count 8 minutes"
    a = []
    for i in range(0,n+1):
        print(i)
        a.append(bin(i).count('1'))
    return a
print(count(5))
