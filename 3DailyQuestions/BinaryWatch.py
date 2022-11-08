class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        answer = []
        for hour in range(12):
            for minute in range(60):
                if( bin(hour).count("1") + bin(minute).count("1") == turnedOn):
                    minu = "0" + str(minute)
                    answer.append(str(hour) + ":" + minu[-2:])
        return answer
