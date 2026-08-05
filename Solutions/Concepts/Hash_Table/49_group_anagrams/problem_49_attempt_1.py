from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1 or len(strs) == 0: return [strs]
        words = []
        groups = []
        for word in strs:
            table = {}
            for char in word:
                if char in table: 
                    table[char] += 1
                else:
                    table[char] = 1
            
            if len(groups) == 0:
                groups.append([table])
                words.append([word])
                continue
            
            added = False 
            for i in range(len(groups)):
                if groups[i][0] == table:
                    groups[i].append(table)
                    words[i].append(word)
                    added = True
                    break
            if not added:
                groups.append([table])
                words.append([word])

        return words