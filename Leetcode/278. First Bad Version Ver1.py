# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n == 1 and isBadVersion(1)) or isBadVersion(1):
            return 1
        left = 1
        right = n
        while True:
            mid1 = (left + right) // 2
            mid2 = mid1 + 1
            if not isBadVersion(mid1) and isBadVersion(mid2):
                return mid2
            elif isBadVersion(mid1) and isBadVersion(mid2):
                right = mid1 - 1
            else:
                left = mid1 + 1
