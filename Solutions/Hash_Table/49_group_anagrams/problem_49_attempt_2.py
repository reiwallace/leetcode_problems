from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1 or len(strs) == 0: return [strs]
        words = {}
        for word in strs:
            total = 0
            for char in word:
                total += ord(char)
            if total in words: 
                words[total] += [word]
            else:
                words[total] = [word]

        groups = []
        for value in words:
            groups.append(words[value])

        return groups