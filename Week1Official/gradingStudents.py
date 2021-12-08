def grade(grades):
    a = []
    for i in grades:
        if(i%5 == 0):
            a.append(i)
        elif((5 - (i%5))<3 and i >= 38):
            a.append(i+(5 - (i%5)))
        else:
            a.append(i)
    return a
print(grade([73,67,38,33]))
        