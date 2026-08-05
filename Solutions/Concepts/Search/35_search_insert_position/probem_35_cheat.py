from bisect import bisect_left
from typing import List

class Solution:
    def searchInsert(self, a: List[int], t: int) -> int:
        return bisect_left(a,t)