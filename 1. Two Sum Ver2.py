class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            try:
                x = target - nums[i]
                j = nums.index(x, i+1)
            except:
                continue
            return [i, nums.index(x, i+1)]


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 5, 5, 10], 10))
