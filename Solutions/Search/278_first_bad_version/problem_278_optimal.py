class Solution:
    def firstBadVersion(self, n: int, bad) -> int:
        def isBadVersion(n):
            if n >= bad:
                return True
            else:
                return False
        bounds = [0, n]
        while bounds[0] < bounds[1]:
            mid = (bounds[0] + bounds[1]) // 2
            if isBadVersion(mid):
                bounds[1] = mid
            else:
                bounds[0] = mid + 1
        return bounds[0]
    