class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while True:
            if right >= left:
                mid = (right + left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                return left


if __name__ == "__main__":
    arr = [-1, 0, 3, 5, 12]
    tar = 9
    s = Solution()
    print(s.searchInsert(arr, tar))
