class Solution:
    def numberToWords(self, num: int) -> str:
        ones = ['Zero', 'One', 'Two', 'Three', 'Four',
                'Five', 'Six', 'Seven', 'Eight', 'Nine']
        one_tens = ['Ten', "Eleven", "Twelve", "Thirteen", "Fourteen",
                    "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ['', '', 'Twenty', 'Thirty', "Forty",
                "Fifty", "Sixty", "Seventy", "Eighty", 'Ninety']
        levels = ['', '', 'Hundred', 'Thousand', 0, 0,
                  'Million', 0, 0, 'Billion', 0, 0, 'Trillion']

        num = str(num)
        if len(num) == 1:
            return ones[int(num[0])]
        if len(num) == 2:
            lead = tens[int(num[0])]
            if int(num[0]) == 1:
                return one_tens[int(num[1])]
            if int(num[0]) == 0:
                return ones[int(num[1])] if int(num[1]) != 0 else lead
            return lead + " " + ones[int(num[1])] if int(num[1]) != 0 else lead
        if len(num) == 3:
            lead = ones[int(num[0])] if int(num[0]) != 0 else ''
            trail = self.numberToWords(num[1:])
            if trail:
                return lead + " " + levels[len(num) - 1] + " " + trail if lead else trail
            else:
                return lead + " " + levels[len(num) - 1] if lead else lead

        mod = len(num) % 3
        level_access = 0
        if mod != 0:
            level_access = len(num) - mod
        else:
            level_access = len(num) - 3
            mod = 3

        lead = self.numberToWords(num[:mod])
        tail = self.numberToWords(num[mod:])
        
        if lead:
            return lead + " " + levels[level_access] + " " + tail if tail else lead + " " + levels[level_access]
        else:
            return tail if tail else ''
