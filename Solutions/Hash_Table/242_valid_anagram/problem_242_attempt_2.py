class Solution:
    # Time Complexity O(nlogn), Space Complexity O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)