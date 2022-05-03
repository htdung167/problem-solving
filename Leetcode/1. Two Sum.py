class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = 0
        b = 1
        len_nums = len(nums)
        for i in range(len_nums - 1):
            for j in range(i + 1, len_nums):
                if i + j == target:
                    a = i
                    b = j
                    break
        return [a, b]
        