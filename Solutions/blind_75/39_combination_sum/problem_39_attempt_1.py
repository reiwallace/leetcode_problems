from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backTrack(start, target, path):
            if target == 0:
                ans.append(path)
                return
            elif target < 0:
                return
            for i in range(start, len(candidates)):
                backTrack(i, target - candidates[i], path + [candidates[i]])

        ans = []
        backTrack(0, target, [])