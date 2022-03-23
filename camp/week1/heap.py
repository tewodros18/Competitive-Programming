#User function Template for python3
class Solution:
    #Heapify function to maintain heap property.
    def __init__(self):
        self.heap = []

    def leftchild(self,index):
        return 2*index +1
    def rightchild(self,index):
        return 2*index+2
    def parent(self,index):
        parentindex = (index-1)//2
        return parentindex
    def insert(self,element):
        self.heap.append(element)
        newelem = len(self.heap) - 1
        while(True):
            
            prnt = self.parent(newelem)
            if(prnt<0):
                break
            if(self.heap[newelem] < self.heap[prnt]):
                (self.heap[newelem],self.heap[prnt])=(self.heap[prnt],self.heap[newelem])
                newelem = prnt
            else:
                break
    def upheap(self,index):
        elemindex = index
        while(True):
            prnt = self.parent(elemindex)
            if(prnt<0):
                break
            if(self.heap[elemindex] < self.heap[prnt]):
                (self.heap[elemindex],self.heap[prnt])=(self.heap[prnt],self.heap[elemindex])
                elemindex = prnt
            else:
                break
    def downheap(self,index):
        elemindex = index
        while(True):
            leftchild = self.leftchild(elemindex)
            rightchild = self.rightchild(elemindex)
            if(leftchild > len(self.heap) - 1 and rightchild > len(self.heap) - 1):
                break
            if(leftchild <= len(self.heap) - 1 and rightchild > len(self.heap) - 1):
                if(self.heap[elemindex] > self.heap[leftchild]):
                    (self.heap[elemindex],self.heap[leftchild])=(self.heap[leftchild],self.heap[elemindex])
                    elemindex = leftchild
                    break
            if(self.heap[leftchild] < self.heap[rightchild]):
                if(self.heap[elemindex] > self.heap[leftchild]):
                    (self.heap[elemindex],self.heap[leftchild])=(self.heap[leftchild],self.heap[elemindex])
                    elemindex = leftchild
                else:
                    break
            elif(self.heap[leftchild] > self.heap[rightchild]):
                if(self.heap[elemindex] > self.heap[rightchild]):
                    (self.heap[elemindex],self.heap[rightchild])=(self.heap[rightchild],self.heap[elemindex])
                    elemindex = rightchild
                else:
                    break
            else:
                break
    def remove(self,index):
        if(index > len(self.heap)):
            return None 
        (self.heap[index],self.heap[len(self.heap) - 1])=(self.heap[len(self.heap) - 1],self.heap[index])
        self.heap.pop()
        if(self.heap[index] < self.heap[self.parent(index)] and self.parent(index) > 0):
            self.upheap(index)
        else:
            self.downheap(index)
    def update(self,index,value):
        self.heap[index] = value
        if(self.heap[index] < self.heap[self.parent(index)]):
            self.upheap(index)
        else:
            self.downheap(index)
    def getmin(self):
        if(len(self.heap)==0):
            return None
        return self.heap[0]
    def heapify(self,arr, n, i):
        self.heap = arr
        for i in range(n-1,0,-1):
            self.upheap(i)
        return self.heap
        # code here
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        pass
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.heapify(arr, n, 5)
        
            

#[1,30,50,200,300]
a = Solution()
#a.insert(1)
#a.HeapSort([3,5,4,6,7], 5)
print(a.heapify([4,1,3,9,7], 5, 0))

