def fizz(num):
    a = []
    for i in range(1,num+1):
        if (i%3 == 0 and i%5 == 0):
            a.append("FizzBuzz")
        elif(i%3 == 0):
            a.append("Fizz")
        elif(i%5 == 0):
            a.append("buzz")
        else:
            a.append()
    return a
print(fizz(3))