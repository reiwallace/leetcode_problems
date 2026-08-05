from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) < 1: return [newInterval]
        done = False
        ans = []
        i = 0
        maxIdx = len(intervals)
        if newInterval[1] < intervals[0][0]:
            ans.append(newInterval)
            return ans + intervals

        while i < maxIdx:
            if newInterval[0] < intervals[i][0] and newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                ans += intervals[1:]
                return ans

            if intervals[i][1] >= newInterval[0]:
                temp = [min(newInterval[0], intervals[i][0]), max(intervals[i][1], newInterval[1])]
                i += 1
                while i < maxIdx and intervals[i][0] <= temp[1]:
                    temp[1] = max(intervals[i][1], temp[1])
                    i += 1
                ans.append(temp)
                ans += intervals[i:]
                done = True
                break
            else:
                ans.append(intervals[i])
                i += 1

        if not done:
            ans.append(newInterval)

        return ans