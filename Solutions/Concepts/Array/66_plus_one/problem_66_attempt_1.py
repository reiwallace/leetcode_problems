class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dig = len(digits) - 1
        digits[dig] += 1
        while digits[dig] > 9:
            digits[dig] = 0
            dig -= 1
            if dig < 0:
                digits.insert(0, 1)
                break
            digits[dig] += 1
        return digits