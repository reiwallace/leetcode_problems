class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        candySet = set()
        size = len(candyType) // 2

        for candy in candyType:
            candySet.add(candy);

        if len(candySet) < size:
            return len(candySet)
        else:
            return size