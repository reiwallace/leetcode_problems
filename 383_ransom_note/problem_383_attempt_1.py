class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for letter in ransomNote:
            search_letter = magazine.find(letter)
            if search_letter >= 0:
                magazine = magazine.replace(letter, "", 1)
            else:
                return False
        return True