class Solution:
    def getSum(self, a: int, b: int) -> int:
        num = 0
        carry = 0
        for i in range(32):
            Abit = (a >> i) & 1
            Bbit = (b >> i) & 1
            if Abit and Bbit:
                if carry:
                    num |= 1 << i
                else:
                    carry = 1
            elif Abit or Bbit:
                if not carry:
                    num |= 1 << i
            elif carry:
                num |= 1 << i
                carry = 0

        if num >= (1 << 31):
            num -= (1 << 32)
        return num
            
