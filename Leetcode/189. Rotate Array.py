class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if len(nums) != 1 and k != 0:
            arr_t = nums[-k:] + nums[:len(nums) - k]
            for i in range(len(arr_t)):
                nums[i] = arr_t[i]
        