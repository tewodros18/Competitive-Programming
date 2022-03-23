class Solution:
    def largestNumber(self, a: List[int]) -> str:
        def BubbleSort(a): 
            length_of_list = len(a)
            while(True):
                swapped = False
                for i in range(1,length_of_list):
                    if (int(a[i-1]+a[i])<int(a[i]+a[i-1])):
                        (a[i-1],a[i]) = (a[i],a[i-1])
                        swapped = True
                if(not swapped):
                    break          
            return a 
        a = [ str(i) for i in a]
        a = BubbleSort(a)
        if a.count("0") == len(a):
            return "0"
        result = ''
        for i in a:result+=i
        return result