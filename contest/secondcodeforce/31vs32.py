from collections import deque
testcases = int(input())
tests = []
for i in range(testcases):
    tests.append(int(input()))
def bfs(start,target):
    result = []
    queue = deque([start])
    level_count = 0
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            current_node = queue.popleft()
            if(current_node == target):
                return (level_count)
            if current_node + 4 <= target + 4:
                queue.append(current_node + 4 )
                level_count += 1
            if current_node - 1 >= target:
                queue.append(current_node - 1)
                level_count += 1
for i in tests:
    a = bfs(31,i)
    b = bfs(32, i)
    if(a<b):
        print(31)
    else:
        print(32)

