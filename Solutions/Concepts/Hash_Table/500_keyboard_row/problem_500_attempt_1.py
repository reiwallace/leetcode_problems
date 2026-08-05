from typing import List

# Time complexity O(n * k) (total letters across words), Space complexity O(1)
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [{"q" : 1, "w" : 1, "e" : 1, "r" : 1, "t" : 1, "y" : 1, "u" : 1, "i" : 1, "o" : 1, "p" : 1}, 
                {"a" : 1, "s" : 1, "d" : 1, "f" : 1, "g" : 1, "h" : 1, "j" : 1, "k" : 1, "l" : 1}, 
                {"z" : 1, "x" : 1, "c" : 1, "v" : 1, "b" : 1, "n" : 1, "m" : 1}]
        
        ans = []

        for word in words:
            idx = 0
            for row in rows:
                if word[0].lower() in row: break
                idx += 1
            skip = False
            for letter in word:
                if not letter.lower() in rows[idx]:
                    skip = True
                    break
            if not skip:
                ans.append(word)

        return ans
            

