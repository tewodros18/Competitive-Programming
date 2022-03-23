a = input().split()
height = int(a[0])
width = int(a[1])
stone = int(a[2])
heightCount = 0
fc = 0
count = 0
while(heightCount<height):
    if(fc>=width):
        heightCount+=stone
        fc=0
    count+=1
    fc+=stone
    
print(count-1)


    