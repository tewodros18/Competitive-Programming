import math
def angle_to(point):
    return math.atan2(point[1], point[0])
def outerTress(trees):
    stack = []
    lowest_point = [0,100]
    #step on find the lowest y-coordinate and left most point,called point P0
    for i in trees:
        if i[1] < lowest_point[1]:
            lowest_point = i
        elif i[1] == lowest_point[1] and i[0] < lowest_point[0]:
            lowest_point = i
    sorted_points = trees

    for point in sorted_points:
        while len(stack) > 1 and CCW(next_to_top(stack), top(stack), point):
            stack.pop()
        stack.append(point)
    print(stack)
def next_to_top(stack):
    #return second to top element without altering stack
    if (len(stack) > 1):
        return (stack[len(stack) - 2])
def top(stack):
    #return top element with out altering stack
    if (len(stack) > 0):
        return (stack[len(stack) - 1]) 
def CCW(p1,p2,p3):
    result = ((p2[0] - p1[0])*(p3[1]-p1[1])) - ((p2[1] - p1[1])*(p3[0] - p1[0]))
    return result

def low(trees):
    lowest_point = [0,100]
    for i in trees:
        if i[1] < lowest_point[1]:
            lowest_point = i
        elif i[1] == lowest_point[1] and i[0] < lowest_point[0]:
            lowest_point = i
    print(lowest_point)

outerTress([[2, 0], [4, 2], [1, 1], [2, 2], [3, 3], [2, 4]])