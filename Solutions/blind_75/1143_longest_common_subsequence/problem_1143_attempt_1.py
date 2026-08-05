class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        map1 = {}
        for i in range(len(text1)):
            if text1[i] in map1:
                map1[text1[i]].append(i)
            else:
                map1[text1[i]] = [i]

        subsequences = []
        for i in range(len(text2)):
            char = text2[i]
            if char in map1 and len(map1[char]) > 0:
                idx = map1[char].pop(0)
                noValid = True
                for subsequence in subsequences:
                    if subsequence[-1] < idx:
                        subsequence.append(idx)
                        noValid = False
                if noValid:
                    subsequences.append([idx])

        longest = 0
        for subsequence in subsequences:
            print(subsequence)
            if len(subsequence) > longest:
                longest = len(subsequence)

        return longest
                
