from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        ans = [1, 0]
        for c in s:
            if ans[1] + widths[ord(c) - 97] > 100:
                ans[0] += 1
                ans[1] = widths[ord(c) - 97]
            else:
                ans[1] += widths[ord(c) - 97]
        
        return ans