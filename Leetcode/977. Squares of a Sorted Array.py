class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numss = [-k if k < 0 else k for k in nums]
        numss.sort()
        return [k*k for k in numss]
