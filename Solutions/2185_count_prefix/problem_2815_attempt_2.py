from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        pref_len = len(pref)
        for word in words:
            if word[:pref_len] == pref:
                count += 1
        return count