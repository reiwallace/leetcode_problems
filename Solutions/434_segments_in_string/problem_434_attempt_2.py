class Solution:
    # O(n) Complexity
    def countSegments(self, s: str) -> int:
        segements = 0
        inSegement = False
        for char in s:
            if char == " ":
                if inSegement:
                    segements += 1
                    inSegement = False
                    continue
                else:
                    continue
            else:
                inSegement = True
        if inSegement: segements += 1

        return segements