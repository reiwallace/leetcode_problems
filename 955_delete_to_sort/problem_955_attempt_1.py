from typing import List

class Solution:
    

    def minDeletionSize(self, strs: List[str]) -> int:
        outOfOrder = True
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        deletions = 0

        while outOfOrder:    
            previousValue = None
            for string in strs:
                if previousValue == None:
                    previousValue = string[0]
                else:
                    if alphabet.index(previousValue) < alphabet.index(string[0]):
                        previousValue = string[0]
                        outOfOrder = False
                        continue
                    elif alphabet.index(previousValue) == alphabet.index(string[0]):
                        while alphabet.index(strs[strs.index(string) - 1][1]) > alphabet.index(string[1]):
                            for i in range(len(strs)):
                                strs[i] = strs[i][0] + strs[i][2:]
                            string = string[0] + string[2:]
                            deletions += 1
                            if len(strs[0]) == 1:
                                return deletions
                        
                    else:
                        if len(string) == 1:
                            return deletions + 1
                        else: 
                            for i in range(len(strs)):
                                strs[i] = strs[i][1:]
                            deletions += 1
                            outOfOrder = True
                            break                
        return deletions