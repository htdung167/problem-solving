class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic.keys():
                return [dic[nums[i]], i]
            sub = target - nums[i]
            dic[sub] = i
            print(dic)


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 10], 9))
