class DetectSquares:
    def __init__(self):
        self.ptsDict = defaultdict(int)
    def add(self, point):
        point = (point[0], point[1])
        if point in self.ptsDict:
            self.ptsDict[point] += 1
        else:
            self.ptsDict[point] = 1
    def count(self, point) -> int:
        point = (point[0], point[1])
        count = 0
        for k, cnt in self.ptsDict.items():
            if abs(k[0] - point[0]) != abs(k[1] - point[1]):
                continue
            if k[1] == point[1] or k[0] == point[0]:
                continue
            if (k[0], point[1]) in self.ptsDict and (point[0], k[1]) in self.ptsDict:
                count += cnt * self.ptsDict[(k[0], point[1])] * self.ptsDict[(point[0], k[1])]
        return count
