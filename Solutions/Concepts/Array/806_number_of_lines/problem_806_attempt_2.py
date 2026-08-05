from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        ans = [1, 0]
        for c in s:
            cWidth = widths[ord(c.lower()) - 97]
            if ans[1] + cWidth > 100:
                ans[0] += 1
                ans[1] = cWidth
            else:
                ans[1] += cWidth
        return ans