class Solution:
    # Time Complexity O(m+n), Space Complexity O(m+n)
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1Len = len(word1)
        word2Len = len(word2)
        mergeArray = []
        for i in range(max(word1Len, word2Len)):
            if i > word1Len - 1: 
                mergeArray.append(word2[i:])
                break
            if i > word2Len - 1:
                mergeArray.append(word1[i:]) 
                break
            mergeArray.append(word1[i] + word2[i])
        return "".join(mergeArray)
