from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        ans = [1, 0]
        for char in s:
            width = widths[ord(char) - 97]
            if ans[1] + width > 100:
                ans[0] += 1
                ans[1] = width
            else:
                ans[1] += width
        return ans
