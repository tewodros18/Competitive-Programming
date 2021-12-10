def sortColors(self, A_list):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length_of_list = len(A_list)
        while(True):
            swapped = False
            for i in range(1,length_of_list):
                if(A_list[i-1] > A_list[i]):
                    (A_list[i-1],A_list[i]) = (A_list[i],A_list[i-1])
                    swapped = True
            if(not swapped):
                break
        return A_list
        