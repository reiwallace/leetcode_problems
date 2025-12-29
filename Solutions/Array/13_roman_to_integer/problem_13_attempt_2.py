class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        romanArr = ["I", "V", "X", "L", "C", "D", "M"]
        intArr = [1, 5, 10, 50, 100, 500, 1000]
        slen = len(s)
        total = 0
        for i in range(slen):
            if i < slen - 1 and roman[s[i]] < roman[s[i+1]]: total -= roman[s[i]]
            else: total += roman[s[i]]

        return total