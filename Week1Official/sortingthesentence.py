class Solution(object):
    def sortSentence(self, s):
        def getnumber(elem):
            return elem[-1]
        """
        :type s: str
        :rtype: str
        """
        mylist = s.split()
        mylist.sort(key=getnumber)
        string = ""
        for i in mylist:
            string += " " + i[:-1]  
        return string[1:]
            
        