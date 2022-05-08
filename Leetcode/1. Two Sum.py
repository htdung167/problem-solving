# Ver 1
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
        
# Ver 2
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


# Ver 3
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
