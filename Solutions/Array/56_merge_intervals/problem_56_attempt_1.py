from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        maxIdx = len(intervals)
        i = 0
        while i < maxIdx:
            upper = ans[-1][1]
            if upper >= intervals[i][0]:
                while i < maxIdx and upper >= intervals[i][0]:
                    ans[-1][1] = max(ans[-1][1], intervals[i][1])
                    i += 1
            else:
                ans.append(intervals[i])
                i += 1

        return ans