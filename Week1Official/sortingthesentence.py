class Solution(object):
    def sortSentence(self, s):
        def getnumber(elem):
            return elem[-1]
        """
        :type s: str
        :rtype: str
        """
        def BubbleSort(A_list):
            length_of_list = len(A_list)
            while(True):
                swapped = False
                for i in range(1,length_of_list):
                    if(A_list[i-1][-1] > A_list[i][-1]):
                        (A_list[i-1],A_list[i]) = (A_list[i],A_list[i-1])
                        swapped = True
                if(not swapped):
                    break
            return (A_list) 
        mylist = s.split()
        mylist = BubbleSort(mylist)
        string = ""
        for i in mylist:
            string += " " + i[:-1]  
        return string[1:]
            
        
        