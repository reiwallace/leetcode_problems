from collections import defaultdict

class Solution:
    # Time Complexity O(n), Space Complexity O(n)
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        table = defaultdict(int)
        for char in stones:
            table[char] += 1

        total = 0
        for char in jewels:
            total += table[char]

        return total