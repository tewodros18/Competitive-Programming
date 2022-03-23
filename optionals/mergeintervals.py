class Solution:
    def merge(self, intervals):
        def getelem(a):
            return a[0]
        intervals.sort(key=getelem)
        def recurse(intervals):
            if(len(intervals) == 1):
                return [intervals[0]]
            privious = recurse(intervals[1:])
            if(privious[0][1]>=intervals[0][0] and privious[0][1]<= intervals[0][1] ):
                privious.insert(0, intervals[0])
                privious.pop(1)
                return privious
            elif(privious[0][0]<=intervals[0][1] ):
                privious.insert(0, [intervals[0][0],privious[0][1]])
                privious.pop(1)
                return privious
            else:
                privious.insert(0, intervals[0])
                return privious
        answer = recurse(intervals)
        main = recurse(answer)
        for i in answer:
            main = recurse(main)
        if(answer[0][1] >= answer[-1][1]):
            return answer[:1]
        return main


print(Solution().merge([[3,3],[4,4],[5,5],[2,3],[1,3],[5,5],[5,5],[5,6],[3,5],[3,3],[4,4],[4,4]]))