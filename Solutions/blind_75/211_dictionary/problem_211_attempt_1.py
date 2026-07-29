class WordDictionary:

    def __init__(self):
        self.words = {}
        self.chars = {}
        
    def addWord(self, word: str) -> None:
        self.words[word] = 1
        curTable = self.chars
        for char in word:
            if not char in curTable:
                curTable[char] = {}
            curTable = curTable[char]


    def search(self, word: str) -> bool:
        if "." in word:
            return self.searchChars(self.chars, 0, word, "")
        else:
            return word in self.words


    def searchChars(self, table, idx, word, constructedWord):
        if idx > len(word) - 1:
            return constructedWord in self.words
        if word[idx] == ".":
            ans = False
            for char in table:
                ans |= self.searchChars(table[char], idx + 1, word, constructedWord + char)
            return ans
        elif word[idx] in table:
            return self.searchChars(table[word[idx]], idx + 1, word, constructedWord + word[idx])
        else:
            return False
