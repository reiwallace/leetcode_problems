class Solution:
    def countAndSay(self, n: int) -> str:
        def sequence(value):
            currentNum = value[0]
            newString = ""
            start = 0
            end = 0
            for num in value:
                if currentNum != num:
                    newString = newString + str(end - start) + str(currentNum)
                    currentNum = num
                    start = end
                end += 1

            return newString + str(end - start) + str(currentNum)

        value = "1"
        for i in range(n - 1):
            value = sequence(value)
        return value
