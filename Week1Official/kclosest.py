import math
def kClosest(A_list,k):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length_of_list = len(A_list)
        while(True):
            swapped = False
            for i in range(1,length_of_list):
                if(math.sqrt(math.pow(A_list[i-1][0],2) + math.pow(A_list[i-1][1],2)) > math.sqrt(math.pow(A_list[i][0],2) + math.pow(A_list[i][1],2))):
                    (A_list[i-1],A_list[i]) = (A_list[i],A_list[i-1])
                    swapped = True
            if(not swapped):
                break
        if(math.sqrt(abs(A_list[0][0] * A_list[0][1])) == math.sqrt(abs(A_list[-1][0] * A_list[-1][1]))):
            A_list.reverse()
            return A_list
        return A_list
print(kClosest([[2,2],[2,2],[2,2],[2,2],[2,2],[2,2],[1,1]],1))
